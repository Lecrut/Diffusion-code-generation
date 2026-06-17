import json
import logging
from pathlib import Path
from typing import List
def setup_logging(config_file: str) -> None:
    config = {}
    if Path(config_file).exists():
        with open(config_file, 'r') as f:
            try:
                config = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                logging.error("Failed to load configuration file. Using defaults.")
    log_level = getattr(logging, str(config.get('level', 'INFO')))
    format_str = " %(asctime)s - %(name)s - %(levelname)s - %(message)s" if config.get('format') else None
    handler = logging.StreamHandler()
    formatter = logging.Formatter(format_str)
    handler.setFormatter(formatter)
    logger = logging.getLogger("StringChecker")
    logger.setLevel(log_level)
    if not hasattr(logger, '_initialized'):
        for h in list(logger.handlers):
            logger.removeHandler(h)
        logger.addHandler(handler)
        logger._initialized = True
def load_lists(file_path: str) -> List[List[str]]:
    if not Path(file_path).exists():
        raise FileNotFoundError(f"Lists configuration file '{file_path}' does not exist.")
    with open(file_path, 'r') as f:
        try:
            data = json.load(f)
            return [item for item in data if isinstance(item, list)]
        except (json.JSONDecodeError, TypeError):
            raise ValueError("Invalid JSON format found in the lists configuration file.")
def check_string_presence(target_str: str, all_lists: List[List[str]]) -> bool:
    for list_item in all_lists:
        if target_str in list_item:
            return True
    return False
if __name__ == '__main__':
    config_file = 'logging_config.json'
    try:
        setup_logging(config_file)
        lists_path = 'lists_data.json'
        all_lists = load_lists(lists_path)
        target_strings = ['apple', 'banana']
        for string in target_strings:
            result = check_string_presence(string, all_lists)
            logger_msg = f"String '{string}' found." if result else f"String '{string}' not found."
    except FileNotFoundError as e:
        logging.error(f"Configuration error: {e}")
    except Exception as e:
        logging.exception("An unexpected error occurred.")