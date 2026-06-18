import json
from typing import Any, Dict, List, Optional
class ConfigTraverser:
    def __init__(self, config_data: Dict[str, Any]):
        self.config = config_data
    def get_nested_value(self, *keys) -> Optional[Any]:
        current = self.config
        for key in keys:
            if isinstance(current, dict):
                if key not in current:
                    return None
                current = current[key]
            else:
                return None
        return current
    def find_all_keys(self, *prefixes) -> List[str]:
        result = []
        def traverse(node: Any, path_parts: List[str]):
            if isinstance(node, dict):
                for key in node.keys():
                    new_path = path_parts + [key]
                    is_match = False
                    for p_key in prefixes:
                        if any(p.lower() == k.lower() for k in new_path[-len(p_key):]):
                            is_match = True
                            break
                    if len(new_path) > 1 and not is_match:
                        continue
                    result.append(".".join(str(k) for k in new_path))
                    traverse(node[key], new_path)
        traverse(self.config, [])
        return sorted(result)
    def validate_structure(self) -> bool:
        required_keys = ["database", "server"]
        if not isinstance(self.config, dict):
            return False
        for key in required_keys:
            value = self.get_nested_value(key)
            if value is None or (isinstance(value, dict) and len(value.keys()) == 0):
                return False
        return True
if __name__ == '__main__':
    sample_config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "credentials": {"username": "admin"}
        },
        "server": {
            "address": "0.0.0.0:8080"
        }
    }
    traverser = ConfigTraverser(sample_config)
    if not traverser.validate_structure():
        print("Configuration validation failed.")
    else:
        keys_found = traverser.find_all_keys()
        for key in keys_found:
            value = traverser.get_nested_value(*key.split("."))
            print(f"{key}: {value}")