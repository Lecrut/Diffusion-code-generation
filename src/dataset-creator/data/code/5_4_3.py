import threading
from typing import Any, Dict
class ThreadSafeDiffCalculator:
    def __init__(self):
        self._lock = threading.Lock()
    def compare_nested_dicts(self, dict1: Dict[str, Any], dict2: Dict[str, Any]) -> list[dict]:
        results = []
        def traverse(d1: Dict[str, Any], d2: Dict[str, Any], path: tuple) -> None:
            if not isinstance(d1, dict) or not isinstance(d2, dict):
                return
            keys_d1 = set(d1.keys())
            keys_d2 = set(d2.keys())
            missing_in_1 = sorted(keys_d1 - keys_d2)
            extra_in_2 = sorted(keys_d2 - keys_d1)
            if missing_in_1:
                for key in missing_in_1:
                    results.append({
                        "path": list(path),
                        "type": "missing",
                        "key": key,
                        "value": None
                    })
            if extra_in_2:
                for key in extra_in_2:
                    results.append({
                        "path": list(path),
                        "type": "extra",
                        "key": key,
                        "value": d2[key]
                    })
            common_keys = keys_d1 & keys_d2
            if not common_keys and missing_in_1 or extra_in_2:
                return 
            for key in sorted(common_keys):
                val1 = d1[key]
                val2 = d2[key]
                diff_entry = {
                    "path": list(path) + [key],
                    "type": None,
                    "value": None
                }
                if type(val1) != type(val2):
                    diff_entry["type"] = "type_mismatch"
                    results.append(diff_entry)
                elif isinstance(val1, dict) and isinstance(val2, dict):
                    with self._lock:
                        sub_results = traverse(val1, val2, tuple(path))
                        if sub_results:
                            for item in sub_results:
                                diff_entry["type"] = "nested_diff"
                                results.append(item)
                elif val1 != val2:
                    diff_entry["type"] = "value_mismatch"
                    results.append(diff_entry)
        traverse(dict1, dict2, tuple())
        return results
if __name__ == '__main__':
    calculator = ThreadSafeDiffCalculator()
    sample_dict_1 = {
        'a': 10,
        'b': {'c': 5},
        'd': [1, 2]
    }
    sample_dict_2 = {
        'a': 20,
        'b': {'c': 6, 'e': 7},
        'f': None
    }
    differences = calculator.compare_nested_dicts(sample_dict_1, sample_dict_2)
    print("Differences found:")
    for diff in differences:
        if diff['type'] is not None:
            path_str = " -> ".join(str(k) for k in diff['path'])
            value_repr = str(diff.get('value', 'N/A'))
            print(f"Path [{diff['type'].replace('_', '-')}]: {path_str} | Value: {value_repr}")