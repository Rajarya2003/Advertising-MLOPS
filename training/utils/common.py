import os
import sys
import yaml
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
from box import ConfigBox
from training.custom_logging import info_logger, error_logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns the content as a ConfigBox object.
    The ConfigBox is a special type of dictionary that allows you to use the keys as attributes.
    :param path_to_yaml: Path to the yaml file
    :return: ConfigBox object
    """
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file) # This will be loaded as a dict
        info_logger.info(f"yaml file: {path_to_yaml} loaded successfully as {type(content)}")
        return ConfigBox(content) # converting the dict to ConfigBox to use the keys as attributes
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates a list of directories at the given paths.
    :param path_to_directories: List of paths to create the directories
    :param verbose: Whether to log the creation of directories
    :return: None
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            info_logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a given dictionary to a json file at the given path.
    :param path: Path to the json file
    :param data: Dictionary to be saved
    :return: None
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    info_logger.info(f"json file saved at {path}")
