import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
    def load(self) -> Dict[str, Any]:
        try:
            with open(self.config_path, 'r') as f:
                data = json.load(f)
            if not isinstance(data, dict):
                raise ValueError("Configuration must be a JSON object")
            logger.info(f"Successfully loaded configuration from {self.config_path}")
            return data
        except FileNotFoundError:
            logger.warning(f"Config file '{self.config_path}' not found. Using defaults.")
            return self.get_defaults()
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON in '{self.config_path}': {e}")
            raise
    def get_defaults(self) -> Dict[str, Any]:
        default_config = {
            "app_name": "ProductionApp",
            "debug_mode": False,
            "max_retries": 3,
            "timeout_seconds": 60
        }
        logger.info("Using default configuration values")
        return default_config
if __name__ == '__main__':
    loader = ConfigLoader('config.json')
    try:
        config_dict = loader.load()
        print(f"Loaded Configuration for {config_dict.get('app_name', 'Unknown')}")
        if not config_dict['debug_mode']:
            logger.info("Running in production mode with retries enabled.")
    except Exception as e:
        logger.critical(f"Configuration loading failed due to error: {e}")