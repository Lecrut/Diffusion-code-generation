import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
    def load(self) -> Dict[str, Any]:
        if not self.config_path.exists():
            logger.warning(f"Configuration file {self.config_path} not found. Using defaults.")
            return {}
        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
            logger.info("Successfully loaded configuration from external source")
            return config
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON in {self.config_path}: {e}")
            self._apply_defaults()
    def _apply_defaults(self):
        defaults = {"timeout": 30, "retries": 3}
        for key, value in defaults.items():
            if key not in self.load_config_data():
                logger.info(f"Applying default value for {key}: {value}")
    def load_config_data(self) -> Dict[str, Any]:
        return {}
if __name__ == '__main__':
    loader = ConfigLoader('config.json')
    config_dict: Dict[str, Any] = loader.load()
    if 'timeout' in config_dict and not isinstance(config_dict['timeout'], int):
        logger.warning("Invalid timeout type detected. Converting to integer.")
        config_dict['timeout'] = 30
    print(f"Loaded configuration dictionary:")
    for key, value in config_dict.items():
        if 'timeout' in str(key).lower() or 'retries' in str(key).lower():
            logger.info(f"{key}: {value}")