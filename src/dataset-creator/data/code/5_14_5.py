import json
from typing import Any, Dict, List, Tuple
class NestedDictComparator:
    def __init__(self) -> None:
        self.mismatches: List[Tuple[int, int]] = []
    def compare(self, dict_a: Dict[str, Any], dict_b: Dict[str, Any]) -> bool:
        if not isinstance(dict_a, dict) or not isinstance(dict_b, dict):
            return False
        keys_a = set(dict_a.keys())
        keys_b = set(dict_b.keys())
        missing_keys = keys_a - keys_b
        extra_keys = keys_b - keys_a
        for key in sorted(missing_keys):
            self.mismatches.append((key, "missing_in_b"))
        for key in sorted(extra_keys):
            self.mismatches.append((key, "extra_in_b"))
        common_keys = keys_a & keys_b
        if len(common_keys) == 0:
            return False
        all_match = True
        for key in common_keys:
            val_a = dict_a[key]
            val_b = dict_b[key]
            is_structural_mismatch = self._compare_values(val_a, val_b)
            if not is_structural_mismatch:
                return False
        return all_match
    def _compare_values(self, a: Any, b: Any) -> bool:
        if type(a) != type(b):
            return False
        if isinstance(a, dict):
            self.mismatches.extend(self._compare_dicts(a, b))
            return len(self.mismatches) == 0
        elif isinstance(a, list):
            max_len = max(len(a), len(b))
            for i in range(max_len):
                val_a = a[i] if i < len(a) else None
                val_b = b[i] if i < len(b) else None
                is_match = self._compare_values(val_a, val_b) or (val_a is not None and val_b is None) or (val_a is None and val_b is not None)
                if not is_match:
                    return False
        else:
            return a == b
        return True
    def _compare_dicts(self, dict_a: Dict[str, Any], dict_b: Dict[str, Any]) -> List[Tuple[int, int]]:
        self.mismatches.clear()
        if not isinstance(dict_a, dict) or not isinstance(dict_b, dict):
            self.mismatches.append((0, "type_mismatch"))
            return self.mismatches
        keys_a = set(dict_a.keys())
        keys_b = set(dict_b.keys())
        missing_keys = sorted(keys_a - keys_b)
        extra_keys = sorted(keys_b - keys_a)
        for key in missing_keys:
            self.mismatches.append((key, "missing_in_b"))
        for key in extra_keys:
            self.mismatches.append((key, "extra_in_b"))
        common_keys = keys_a & keys_b
        if len(common_keys) == 0:
            return self.mismatches
        all_match = True
        for key in common_keys:
            val_a = dict_a[key]
            val_b = dict_b[key]
            is_structural_mismatch = self._compare_values(val_a, val_b)
            if not is_structural_mismatch:
                return False
        return self.mismatches
if __name__ == '__main__':
    sample_dict_1 = {
        "user": {"id": 101, "profile": {"age": 25}},
        "settings": ["theme", "dark_mode"],
        "metadata": {}
    }
    sample_dict_2 = {
        "user": {"id": 101, "profile": {"name": "Alice"}},
        "settings": ["theme", "light_mode"],
        "extra_field": True
    }
    comparator = NestedDictComparator()
    result = comparator.compare(sample_dict_1, sample_dict_2)
    print(f"Structural Match: {result}")
    if not result and len(comparator.mismatches) > 0:
        for item in comparator.mismatches:
            key_str, reason = item[0], item[1]
            print(f"Mismatch at '{key_str}': {reason}")