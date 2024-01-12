import os
import sys
from sklearn.metrics import mean_squared_error,mean_absolute_error
# from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import pickle
from src.logger.logger import logging
from src.utils.utils import  save_object,load_object
from src.exception.exceptions import customexception
from dataclasses import dataclass
from pathlib import Path

@dataclass
class ModelEvaluationConfig:
    pass
class ModelEvaluation:
    def __init__(self):
        pass
    try:
        pass
    except Exception as e:
        logging.info()
        raise customexception