import pathlib
import pickle

from sklearn.base import BaseEstimator


def saveModel(model: BaseEstimator, model_path: pathlib.StrPath) -> None:
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

def loadModel(model_path: pathlib.StrPath) -> BaseEstimator:
    with open(model_path, 'rb') as f:
        return pickle.load(f)