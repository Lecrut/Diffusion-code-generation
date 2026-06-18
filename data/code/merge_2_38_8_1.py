import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional
def setup_logging(config_path: str) -> None:
    log_dir = Path("logs") / "config"
    log_dir.mkdir(parents=True, exist_ok=True)
    handler = logging.FileHandler(log_dir / f"{Path(config_path).stem}.log", mode="a")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
def load_config_file(path: str, fallback_value: Any = None) -> Dict[str, Any]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning(f"Config file {path} not found. Using default values.")
        if fallback_value is None:
            raise ValueError("No config provided and no fallback defined")
        return fallback_value.copy()
def create_dictionary_from_config(config_path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    setup_logging(config_path)
    logger = logging.getLogger(__name__)
    try:
        config_data = load_config_file(config_path, {})
        merged_dict = defaults.copy()
        for key in config_data.keys():
            if key not in merged_dict and isinstance(config_data[key], dict):
                nested_key_list = list(config_data[key].keys())
                logger.info(f"Found {len(nested_key_list)} keys: {nested_key_list}")
                for k, v in config_data[key].items():
                    if key not in merged_dict or isinstance(merged_dict.get(key), dict):
                        nested = merged_dict.setdefault(key, {})
                        if isinstance(v, (dict, list)):
                            logger.debug(f"Key '{k}' has type {type(v).__name__}")
                            for nk, nv in v.items():
                                if not isinstance(nv, str) and len(str(nv)) > 0:
                                    nested[nk] = json.dumps(nv)
                        else:
                            logger.debug(f"Key '{key}' has type {type(v).__name__}")
                            for nk, nv in v.items():
                                if not isinstance(nv, str):
                                    nested[nk] = json.dumps(nv)
        return merged_dict
    except Exception as e:
        logger.error(f"Error loading configuration from {config_path}: {str(e)}")
        raise
if __name__ == '__main__':
    sample_config = {"app": {"host": "localhost", "port": 8080}}
    defaults = {
        "database": {"driver": "sqlite3"},
        "cache": {"enabled": True},
        "logging": {"level": "INFO"}
    }
    result_dict = create_dictionary_from_config("config.json", defaults)
    print(json.dumps(result_dict, indent=2))