import logging
from typing import Any, Dict, List, Optional
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def search_nested_dict(data: Any, target: Any, path: str = "") -> bool:
    if data is None or isinstance(data, dict):
        for key in data.keys():
            current_path = f"{path}.{key}" if path else str(key)
            value = data[key]
            if target == value and (not isinstance(value, (dict, list)) or not search_nested_dict(value, target, current_path)):
                logger.info(f"Target '{target}' found at: {current_path}")
                return True
            elif isinstance(data[key], dict):
                if search_nested_dict(data[key], target, current_path):
                    return True
    elif isinstance(data, list) or isinstance(data, tuple):
        for index, item in enumerate(data):
            current_path = f"{path}[{index}]"
            if target == item and (not isinstance(item, (dict, list)) or not search_nested_dict(item, target, current_path)):
                logger.info(f"Target '{target}' found at: {current_path}")
                return True
            elif isinstance(item, dict):
                if search_nested_dict(item, target, current_path):
                    return True
    else:
        logger.info(f"Target '{target}' found at root level")
    logger.warning(f"Target '{target}' not found in structure.")
    return False
if __name__ == '__main__':
    sample_data = {
        "user": {
            "id": 101,
            "details": {
                "name": "Alice",
                "roles": ["admin", "editor"],
                "metadata": {"active": True}
            }
        },
        "system": {
            "status": "online"
        }
    }
    test_cases = [101, 999, "Alice"]
    for item in test_cases:
        logger.info(f"\n--- Searching for '{item}' ---")
        result = search_nested_dict(sample_data, item)