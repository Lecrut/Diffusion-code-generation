import json
from typing import Any, Dict, List, Tuple
class NestedDictComparator:
    def __init__(self):
        self.differences = []
    def compare(self, dict1: Dict[str, Any], dict2: Dict[str, Any]) -> None:
        if not isinstance(dict1, dict) or not isinstance(dict2, dict):
            return
        keys_dict1 = set(dict1.keys())
        keys_dict2 = set(dict2.keys())
        missing_keys_in_1 = sorted(keys_dict1 - keys_dict2)
        extra_keys_in_2 = sorted(keys_dict2 - keys_dict1)
        for key in missing_keys_in_1:
            self.differences.append(f"Key '{key}' exists only in dict 1")
        for key in extra_keys_in_2:
            self.differences.append(f"Key '{key}' exists only in dict 2")
        common_keys = keys_dict1 & keys_dict2
        if not common_keys and missing_keys_in_1 or not common_keys and extra_keys_in_2:
            return
        for key in sorted(common_keys):
            val1, val2 = dict1[key], dict2[key]
            self._compare_values(val1, val2)
    def _compare_values(self, v1: Any, v2: Any) -> None:
        if type(v1) != type(v2):
            return
        if isinstance(v1, dict):
            self.compare(v1, v2)
        elif isinstance(v1, list):
            len_diff = abs(len(v1) - len(v2))
            if len_diff > 0:
                self.differences.append(f"List at current level has length difference of {len_diff}")
            min_len = min(len(v1), len(v2))
            for i in range(min_len):
                self._compare_values(v1[i], v2[i])
    def get_report(self) -> str:
        return "\n".join(f"- {diff}" for diff in self.differences if diff)
if __name__ == '__main__':
    sample_dict_1 = {
        "user": {"id": 101, "profile": {"age": 30}},
        "settings": ["theme", "dark_mode"],
        "metadata": {}
    }
    sample_dict_2 = {
        "user": {"id": 101, "profile": {"name": "Alice"}},
        "settings": ["theme", "notifications"],
        "extra_field": True
    }
    comparator = NestedDictComparator()
    comparator.compare(sample_dict_1, sample_dict_2)
    print(comparator.get_report())