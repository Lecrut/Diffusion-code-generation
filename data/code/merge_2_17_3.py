import logging
from typing import Any, Dict, List, Tuple
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
def find_item_in_nested_dict(data: Dict[str, Any], target: Any) -> bool:
    def _search(current_data: Dict[str, Any]) -> List[Tuple[Any, str]]:
        results = []
        if not isinstance(current_data, dict):
            return results
        key_names = list(current_data.keys())
        for i, (key_name, value) in enumerate(current_data.items()):
            if value == target:
                full_path = " -> ".join(key_names[:i+1]) + f"[{value}] is {target}"
                results.append((True, full_path))
        for key_name in current_data.keys():
            if isinstance(value, dict):
                _search(current_data[key_name])
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        results.extend(_search(item))
        return results
    found = []
    try:
        _results = _search(data)
        return any([result[0] for result in _results]) if _results else False
    except Exception as e:
        logger.exception(f"Error during nested dictionary traversal: {e}")
        raise
if __name__ == '__main__':
    sample_data = {
        "user": {"id": 1, "details": {"username": "alice", "roles": ["admin"]}},
        "product": {"sku": "P001", "inventory": [{"qty": 5}, {"qty": 2}]},
        "settings": None
    }
    target_user = sample_data["user"]["details"]["username"]
    if find_item_in_nested_dict(sample_data, target_user):
        logger.info(f"Target '{target_user}' found in nested structure.")
    else:
        logger.warning(f"Target '{target_user}' not found in any part of the data.")