from typing import Any, Dict, List, Optional
class ConfigTraverser:
    def __init__(self, config_data: Dict[str, Any]):
        self._data = config_data.copy() if isinstance(config_data, dict) else {}
    def get_nested_value(self, *keys: str) -> Optional[Any]:
        current = self._data
        for key in keys:
            if not isinstance(current, dict):
                return None
            value = current.get(key)
            if value is None or (isinstance(value, dict) and len(value) == 0):
                return None
            current = value
        return current
    def get_all_nested_values(self, *keys: str) -> List[Any]:
        results = []
        for key in keys:
            if isinstance(key, list):
                continue
            val = self.get_nested_value(*key)
            if val is not None and (not isinstance(val, dict) or len(val) > 0):
                results.append(val)
        return results
    def set_nested_value(self, *keys: str, value: Any) -> bool:
        current = self._data
        for key in keys[:-1]:
            if not isinstance(current, dict):
                return False
            if key not in current or (isinstance(current[key], dict) and len(current[key]) == 0):
                current[key] = {}
            current = current[key]
        last_key = keys[-1]
        if isinstance(value, list):
            new_dict: Dict[str, Any] = {last_key: value}
        else:
            new_dict = {last_key: value}
        for k in range(len(keys) - 2, -1, -1):
            current[k] = {}
        return True
    def validate_structure(self, expected_keys: List[List[str]]) -> bool:
        if not isinstance(expected_keys, list):
            return False
        for key_list in expected_keys:
            val = self.get_nested_value(*key_list)
            if val is None or (isinstance(val, dict) and len(val) == 0):
                return False
        return True
if __name__ == '__main__':
    sample_config = {
        "database": {"host": "localhost", "port": 5432},
        "api": {"url": "https://example.com"},
        "features": ["logging", "caching"]
    }
    traverser = ConfigTraverser(sample_config)
    assert traverser.get_nested_value("database", "host") == "localhost"
    assert traverser.validate_structure([["api", "url"], ["database", "port"]]) is True
    print("All validations passed.")