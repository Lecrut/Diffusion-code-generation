import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional
def setup_logging(config: Dict[str, Any]) -> None:
    log_level = getattr(logging, config.get("logging", {}).get("level", "INFO"), logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger("config_loader")
    logger.setLevel(log_level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
def load_json_file(file_path: str, fallback_dict: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    if not Path(file_path).exists():
        return fallback_dict or {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            logging.info(f"Successfully loaded configuration from {file_path}")
            return data
    except (json.JSONDecodeError, IOError):
        if fallback_dict is not None:
            logging.warning(
                f"Failed to parse or read {file_path}, using fallback dictionary."
            )
            return fallback_dict
        else:
            raise
def create_dictionary_from_config(
    primary_file: str,
    secondary_files: list[str],
    default_values: Dict[str, Any] = None,
) -> Dict[str, Any]:
    logging.info("Starting configuration load process")
    result: Dict[str, Any] = {}
    if not Path(primary_file).exists():
        logging.warning(f"Primary config {primary_file} missing. Using default values.")
        result.update(default_values or {})
    else:
        loaded_data = load_json_file(primary_file, default_values)
        result.update(loaded_data)
    logging.info(f"Processing {len(secondary_files)} secondary configuration files.")
    for file_path in secondary_files:
        if not Path(file_path).exists():
            continue
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for key, value in data.items():
                if (key not in result and 
                    default_values is None or key in default_values):
                    logging.info(
                        f"Applying configuration from {file_path} for key '{key}'."
                    )
                    result[key] = value
        except Exception as e:
            logging.error(f"Error processing file {file_path}: {e}")
    return result
if __name__ == '__main__':
    primary_file = "/etc/config/app.json"
    secondary_files = ["/etc/config/override1.json", "/etc/config/override2.json"]
    default_dict: Dict[str, Any] = {
        "app_name": "MyApp",
        "debug_mode": False,
        "max_connections": 100
    }
    config_data = create_dictionary_from_config(
        primary_file=primary_file,
        secondary_files=secondary_files,
        default_values=default_dict
    )
    logging.info("Configuration loaded successfully.")
    print(json.dumps(config_data, indent=2))