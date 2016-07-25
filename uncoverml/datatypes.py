import logging

import numpy as np
from uncoverml import validation

log = logging.getLogger(__name__)


class Settings:

    def __repr__(self):
        return str(self.__dict__)


class ExtractSettings(Settings):

    def __init__(self, onehot, x_sets, patchsize):
        self.onehot = onehot
        self.x_sets = x_sets
        self.patchsize = patchsize


class ComposeSettings(Settings):

    def __init__(self, impute, transform, featurefraction, impute_mean, mean,
                 sd, eigvals, eigvecs):
        self.impute = impute
        self.transform = transform
        self.featurefraction = featurefraction
        self.impute_mean = impute_mean
        self.mean = mean
        self.sd = sd
        self.eigvals = eigvals
        self.eigvecs = eigvecs


class CrossValTargets:

    def __init__(self, lonlat, vals, folds=10, seed=None, sort=False):
        N = len(lonlat)
        # we may be given folds already
        if type(folds) == int:
            _, cvassigns = validation.split_cfold(N, folds, seed)
        else:
            cvassigns = folds
        if sort:
            # Get ascending order of targets by lat then lon
            ordind = np.lexsort(lonlat.T)
            self.observations = vals[ordind]
            self.positions = lonlat[ordind]
            self.folds = cvassigns[ordind]
        else:
            self.observations = vals
            self.positions = lonlat
            self.folds = cvassigns
