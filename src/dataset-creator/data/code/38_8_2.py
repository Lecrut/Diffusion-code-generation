import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def load_config_file(filepath: str) -> Optional[Dict[str, Any]]:
    try:
        with open(Path(filepath), "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning(f"Configuration file not found at {filepath}. Fallback to defaults.")
        return None
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON in {filepath}: {e}")
        return None
def create_dictionary(
    config_path: str,
    default_config: Dict[str, Any],
) -> Dict[str, Any]:
    loaded = load_config_file(config_path)
    if not loaded or (loaded is None and Path(config_path).exists()):
        logger.warning("Using fallback configuration.")
        return default_config.copy()
    final_config = default_config.copy()
    for key in list(final_config.keys()):
        try:
            new_value = loaded[key]
            if isinstance(new_value, dict):
                nested_keys = [k for k in final_config.get(key, {}) if not callable(getattr(type(None), f'{key}', None))]                                                           
                if any(isinstance(final_config[key][k], (dict, list)) and loaded[key].get(k) is not None for k in nested_keys):
                    new_value = final_config.get(key, {})
            elif isinstance(new_value, dict):
                pass
        except Exception as e:
            logger.error(f"Error merging config at key {key}: {e}")
    if loaded and Path(config_path).exists():
        for key in list(final_config.keys()):
            new_val = loaded.get(key)
            try:
                final_config[key] = new_val
            except Exception as e:
                logger.error(f"Error updating config at key {key}: {e}")
    return final_config
if __name__ == '__main__':
    default_settings = {"database": "localhost", "port": 5432, "timeout": 10}
    result_dict = create_dictionary("config.json", default_settings)
    print(json.dumps(result_dict))