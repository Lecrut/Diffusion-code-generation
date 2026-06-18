import json
from typing import Any, Dict, List, Optional
class ConfigTraverser:
    def __init__(self, config_data: Dict[str, Any]):
        self._data = config_data
    def get_value(self, path_parts: List[Optional[str]]) -> Any:
        current = self._data
        for part in path_parts:
            if isinstance(part, str):
                key_to_find = part.lower()
                found_keys = [k.lower() for k in current.keys()]
                matches = [k for k in found_keys if k == key_to_find]
                if len(matches) > 1:
                    raise ValueError(f"Multiple keys match '{part}'")
                target_key = next(iter(matches))
            else:
                return None
            if not isinstance(current, dict):
                raise TypeError("Expected dictionary at path part index " + str(path_parts.index(part)))
            current = current.get(target_key)
        return current
    def get_all_values(self, key_pattern: Optional[str] = None) -> List[Dict]:
        results = []
        if not isinstance(self._data, dict):
            return results
        keys_to_check = [k.lower() for k in self._data.keys()]
        if key_pattern is not None and len(key_pattern) > 0:
            pattern_lower = key_pattern.lower()
            matches = []
            def find_matching(data_dict, prefix_len=1):
                nonlocal results
                current_keys = [k.lower() for k in data_dict.keys()]
                matching_top_level = []
                for i, val in enumerate(current_keys[:prefix_len]):
                    if val.startswith(pattern_lower):
                        matching_top_level.append(val)
                results.extend(matching_top_level)
            find_matching(self._data, 1)
        else:
            return self._data.values()
if __name__ == '__main__':
    sample_config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "credentials": {"username": "admin"}
        },
        "api": {
            "endpoint": "/v1/users",
            "timeout": 30
        }
    }
    traverser = ConfigTraverser(sample_config)
    path_result = traverser.get_value(["database", "credentials"])
    print(f"Database Credentials: {path_result}")
    all_values = traverser.get_all_values()
    for val in all_values:
        if isinstance(val, dict):
            print("Config Sections:", list(val.keys()))