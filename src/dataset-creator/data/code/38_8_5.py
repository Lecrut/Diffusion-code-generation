import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional
def setup_logging(log_file: str = "app.log", log_level: int = 20) -> None:
    logger = logging.getLogger("config_loader")
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG if log_level == 20 else logging.INFO)
def load_json_config(file_path: str, fallback_value: Any = None) -> Dict[str, Any]:
    config = {}
    try:
        with open(Path(file_path), "r") as f:
            content = json.load(f)
            if isinstance(content, dict):
                return content
            else:
                raise ValueError("Configuration must be a JSON object.")
    except FileNotFoundError:
        logging.warning(f"File {file_path} not found. Using fallback value.")
        config = fallback_value.copy() if isinstance(fallback_value, dict) else {}
    except json.JSONDecodeError as e:
        error_msg = f"Invalid JSON in {file_path}: {e}"
        logging.error(error_msg)
        config = fallback_value.copy() if isinstance(fallback_value, dict) else {}
    return config
def create_dictionary_from_config(
    primary_file: str,
    secondary_files: list[str],
    default_fallback: Dict[str, Any] | None = None,
    log_level: int = 20,
    log_file: str = "config_loader.log",
) -> Dict[str, Any]:
    setup_logging(log_file=log_file, log_level=log_level)
    logger = logging.getLogger("config_loader")
    config_dict = {}
    if primary_file and Path(primary_file).exists():
        try:
            with open(Path(primary_file), "r") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    for key in default_fallback or {}:
                        if key not in config_dict:
                            config_dict[key] = default_fallback[key]
        except Exception as e:
            logger.error(f"Error loading primary file {primary_file}: {e}")
    else:
        logger.warning(f"Primary configuration file {primary_file} does not exist.")
    for idx, secondary in enumerate(secondary_files):
        try:
            with open(Path(secondary), "r") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    for key in default_fallback or {}:
                        if key not in config_dict and key in data:
                            config_dict[key] = data[key]
        except Exception as e:
            logger.warning(f"Error loading secondary file {secondary}: {e}")
    return config_dict
if __name__ == '__main__':
    primary_file_path = "config_primary.json"
    secondary_files_list = ["config_secondary_1.json", "config_backup.json"]
    default_fallback_data: Dict[str, Any] = {"timeout": 30, "retries": 3}
    final_config = create_dictionary_from_config(
        primary_file=primary_file_path,
        secondary_files=secondary_files_list,
        default_fallback=default_fallback_data,
        log_level=logging.INFO,
        log_file="production.log",
    )
    print("Final Configuration:")
    for key in final_config:
        if isinstance(final_config[key], int):
            print(f"{key}: {final_config[key]}")