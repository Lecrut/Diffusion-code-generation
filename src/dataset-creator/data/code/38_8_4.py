import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional
def setup_logging(log_file: str = "config_loader.log", level: int = logging.INFO) -> None:
    root_logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
    handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    root_logger.addHandler(stream_handler)
    root_logger.setLevel(level)
    return root_logger
def load_config_file(file_path: str, logger: Optional[logging.Logger] = None) -> Dict[str, Any]:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
        if logger:
            logger.info(f"Successfully loaded configuration from {file_path}")
        return config_data
    except FileNotFoundError:
        msg = f"Configuration file not found: {file_path}"
        raise Exception(msg)
    except json.JSONDecodeError as e:
        msg = f"Invalid JSON format in {file_path}: {e.msg}"
        raise ValueError(msg) from None
def create_dictionary_from_config(
    primary_file: str, 
    fallback_files: list[str], 
    default_values: Dict[str, Any] = {},
    logger: Optional[logging.Logger] = None
) -> Dict[str, Any]:
    try:
        config_data = load_config_file(primary_file, logger=logger)
        if logger:
            logger.info(f"Primary config loaded successfully.")
        return default_values | config_data
    except Exception as e:
        fallback_msg = f"Fallback triggered due to error loading primary file ({primary_file}): {e}"
        for i, fallback_path in enumerate(fallback_files):
            try:
                config_data = load_config_file(fallback_path, logger=logger)
                if logger and not primary_file.startswith("primary"):
                    msg_suffix = f" using {fallback_path}"
                return default_values | config_data
            except Exception as e2:
                fallback_msg += f"; Failed to use fallback file ({i+1}): {e2}"
        if logger:
            critical_level = logging.CRITICAL if not primary_file.startswith("primary") else logging.ERROR
            msg_parts = [f"Failed to load configuration from any source."]
            if "Primary config loaded successfully." in fallback_msg or ("fallback triggered" in str(e) and e.args[0] == f"Fallback triggered due to error loading primary file ({primary_file}): {e}"):
                logger.error(f"{msg_parts[-1]}: Primary file failed. All fallbacks exhausted.")
            else:
                logger.critical(msg_parts[-1])
        raise Exception("No valid configuration found after exhausting all sources and defaults.")
if __name__ == '__main__':
    DEFAULT_VALUES = {
        "app_name": "MyApp",
        "debug_mode": False,
        "database_host": "localhost"
    }
    PRIMARY_CONFIG = {
        "app_name": "ProductionApp",
        "debug_mode": True,
        "database_host": "prod-db.example.com"
    }
    FALLBACK_CONFIG_1 = {
        "app_name": "StagingApp",
        "debug_mode": False,
        "log_level": "INFO"
    }
    temp_primary_path = Path("temp_config.json")
    temp_fallback_1_path = Path("fallback_config.json")
    try:
        with open(temp_primary_path, 'w') as f:
            json.dump(PRIMARY_CONFIG, f)
        with open(temp_fallback_1_path, 'w') as f:
            json.dump(FALLBACK_CONFIG_1, f)
        logger = setup_logging(log_file="config_loader.log", level=logging.INFO)
        primary_file = str(temp_primary_path.absolute())
        fallback_files = [str(temp_fallback_1_path.absolute()), "nonexistent.json"]
        final_config_dict = create_dictionary_from_config(
            primary_file=primary_file, 
            fallback_files=fallback_files, 
            default_values=DEFAULT_VALUES, 
            logger=logger
        )
        print(json.dumps(final_config_dict, indent=4))
    finally:
        temp_primary_path.unlink(missing_ok=True)
        temp_fallback_1_path.unlink(missing_ok=True)