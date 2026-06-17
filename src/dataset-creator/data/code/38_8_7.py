import json
import logging
from pathlib import Path
from typing import Dict, Any, Optional
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class ConfigLoader:
    def __init__(self):
        self.configs_cache: Dict[str, Dict] = {}
    def load_from_file(self, file_path: str) -> Optional[Dict]:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            if not isinstance(data, dict):
                logger.error(f"Configuration in {file_path} is not a dictionary.")
                return None
            self.configs_cache[file_path] = data
            logger.info(f"Successfully loaded configuration from {file_path}")
            return data
        except FileNotFoundError:
            logger.warning(f"File {file_path} not found. Attempting fallback...")
            return None
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in {file_path}: {e}. Fallback triggered.")
            return None
    def get_config(self, file_paths: list[str], default_data: Optional[Dict] = None) -> Dict:
        for path in reversed(file_paths):                                       
            if path not in self.configs_cache and Path(path).exists():
                config = self.load_from_file(str(Path(path)))
                if config is not None:
                    return config
        logger.warning("No valid configuration found. Using default.")
        return default_data or {}
if __name__ == '__main__':
    loader = ConfigLoader()
    primary_config_path = "config_primary.json"
    fallback_config_path = "config_fallback.json"
    defaults = {"app_name": "DefaultApp", "debug_mode": False}
    final_config: Dict[str, Any] = loader.get_config([primary_config_path, fallback_config_path], defaults)
    print(f"Loaded configuration for {final_config.get('app_name', 'Unknown')}")