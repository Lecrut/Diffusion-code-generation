import json
from typing import Any, Dict, List, Tuple
class NestedDictComparator:
    def __init__(self):
        self.differences = []
    def compare(self, dict_a: Dict[str, Any], dict_b: Dict[str, Any]) -> None:
        if not isinstance(dict_a, dict) or not isinstance(dict_b, dict):
            return
        keys_a = set(dict_a.keys())
        keys_b = set(dict_b.keys())
        missing_in_a = keys_b - keys_a
        extra_in_a = keys_a - keys_b
        common_keys = keys_a & keys_b
        for key in sorted(missing_in_a):
            self.differences.append(f"Key '{key}' exists in dict B but not in dict A")
        for key in sorted(extra_in_a):
            self.differences.append(f"Key '{key}' exists in dict A but not in dict B")
        for key in common_keys:
            val_a = dict_a[key]
            val_b = dict_b[key]
            if isinstance(val_a, dict) and isinstance(val_b, dict):
                self.compare(val_a, val_b)
            elif type(val_a) != type(val_b):
                self.differences.append(f"Type mismatch for key '{key}': {type(val_a).__name__} vs {type(val_b).__name__}")
            else:
                if isinstance(val_a, (list, tuple)):
                    len_diff = val_a.__len__() - val_b.__len__()
                    self.differences.append(f"Length mismatch for key '{key}': {val_a.__len__()} vs {val_b.__len__()}, diff={len_diff}")
        else:
            if not isinstance(val_a, (list, tuple)):
                if val_a != val_b:
                    self.differences.append(f"Mismatch at key '{key}': {json.dumps(val_a)} vs {json.dumps(val_b)}")
def generate_sample_data() -> Tuple[Dict[str, Any], Dict[str, Any]]:
    data_a = {
        "user": {"id": 101, "name": "Alice", "roles": ["admin"]},
        "settings": {"theme": "dark"},
        "metadata": [
            {"timestamp": "2023-01-01", "status": "active"},
            {"timestamp": "2023-01-02", "status": "pending"}
        ]
    }
    data_b = {
        "user": {"id": 101, "name": "Alice", "roles": ["admin", "editor"]},
        "settings": {"theme": "light"},
        "metadata": [
            {"timestamp": "2023-01-01", "status": "active"}
        ],
        "extra_field": True
    }
    return data_a, data_b
if __name__ == '__main__':
    comparator = NestedDictComparator()
    sample_dict_1, sample_dict_2 = generate_sample_data()
    try:
        comparator.compare(sample_dict_1, sample_dict_2)
        if not comparator.differences:
            print("No differences found.")
        else:
            for diff in comparator.differences:
                print(diff)
    except Exception as e:
        pass