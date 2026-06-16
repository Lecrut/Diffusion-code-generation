import json
from typing import Any, Dict, List, Tuple
class NestedDictComparator:
    def __init__(self):
        self.mismatches: List[Tuple[int, int, str]] = []
    def compare(self, dict_a: Dict[str, Any], dict_b: Dict[str, Any]) -> bool:
        if not isinstance(dict_a, dict) or not isinstance(dict_b, dict):
            return False
        self.mismatches.clear()
        keys_a = set(dict_a.keys())
        keys_b = set(dict_b.keys())
        all_keys = keys_a.union(keys_b)
        for key in sorted(all_keys):
            val_a = dict_a.get(key, None)
            val_b = dict_b.get(key, None)
            if key not in keys_a or key not in keys_b:
                self.mismatches.append((key, "missing", f"Key '{key}' exists only in {'dict_a' if key in keys_a else 'dict_b'}"))
                continue
            if val_a != val_b:
                is_nested = isinstance(val_a, dict) and isinstance(val_b, dict)
                if not is_nested:
                    self.mismatches.append((key, "value_mismatch", f"Values differ at '{key}': {val_a!r} vs {val_b!r}"))
                else:
                    sub_comp = NestedDictComparator()
                    sub_result = sub_comp.compare(val_a, val_b)
                    if not sub_result:
                        self.mismatches.append((f"{key}.", "nested_mismatch", f"Structural differences found in nested object at '{key}'"))
        return len(self.mismatches) == 0
def generate_sample_data() -> Tuple[Dict[str, Any], Dict[str, Any]]:
    sample_a = {
        "id": 12345,
        "metadata": {
            "version": "v2.0",
            "tags": ["active", "verified"],
            "config": {"timeout": 30, "retry_count": 3}
        },
        "items": [
            {"name": "item_1", "status": "completed"},
            {"name": "item_2", "status": "pending"}
        ],
        "nested_deep": {
            "level1": {
                "level2": {
                    "value": 42,
                    "flags": True
                }
            },
            "extra_field": None
        }
    }
    sample_b = {
        "id": 12345,
        "metadata": {
            "version": "v2.0",
            "tags": ["active"],
            "config": {"timeout": 60}
        },
        "items": [
            {"name": "item_1", "status": "completed"},
            {"name": "item_3", "status": "pending"}
        ],
        "nested_deep": {
            "level1": {
                "level2": {
                    "value": 42,
                    "flags": False
                }
            },
            "extra_field": None
        }
    }
    return sample_a, sample_b
if __name__ == '__main__':
    data_a, data_b = generate_sample_data()
    comparator = NestedDictComparator()
    is_identical = comparator.compare(data_a, data_b)
    print(f"Structural Match: {is_identical}")
    if not is_identical and len(comparator.mismatches) > 0:
        for idx, (key, reason, details) in enumerate(comparator.mismatches):
            print(f"Mismatch #{idx + 1}: Key '{key}' - Reason: {reason} | Details: {details}")