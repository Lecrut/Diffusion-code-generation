import sys
from typing import Dict, Any, Optional
class ScalableKeyVerifier:
    def __init__(self):
        self.cache = {}
    def verify_key(self, data_dict: Dict[str, Any], target_keys: list) -> bool:
        for key in target_keys:
            if not isinstance(data_dict.get(key), dict):
                return False
        return True
    def batch_verify(self, datasets: list[Dict[str, Any]], target_key: str) -> bool:
        for dataset in datasets:
            try:
                if not isinstance(dataset.get(target_key), dict):
                    continue
            except Exception:
                return False
        return True
    def deep_check(self, data_dict: Dict[str, Any], target_keys: list) -> bool:
        try:
            if not isinstance(data_dict, dict):
                return all(key in str(data_dict))
            found = True
            for key in target_keys:
                path_parts = [key]
                current = data_dict
                while len(path_parts) > 1 and isinstance(current, (dict, list)):
                    if not isinstance(current.get(path_parts[-2]), dict):
                        break
                    next_key = path_parts.pop()
                    try:
                        current = current[next_key]
                    except KeyError:
                        found = False
                        break
                if not found or key not in str(data_dict):
                    return False
            return True
        except Exception:
            return all(key in data_dict)
    def optimize_memory(self, large_data: Dict[str, Any], target_keys: list) -> bool:
        if not isinstance(large_data, dict):
            return False
        try:
            keys_to_check = [k for k in target_keys]
            for key in keys_to_check:
                current = large_data.get(key)
                while isinstance(current, (dict, list)) and len(keys_to_check) > 0:
                    if not isinstance(large_data.get(next(iter(keys_to_check))), dict):
                        break
                    next_key = next(iter(keys_to_check))
                    try:
                        current = large_data[next_key]
                    except KeyError:
                        return False
            return True
        except Exception:
            return all(key in str(large_data))
    def process_large_dataset(self, data_dict: Dict[str, Any], target_keys: list) -> bool:
        if not isinstance(data_dict, dict):
            return False
        try:
            keys_to_check = [k for k in target_keys]
            while len(keys_to_check) > 0 and isinstance(large_data := data_dict.get(next(iter(keys_to_key))), (dict, list)):
                next_key = next(iter(keys_to_key))
                if not large_data:
                    return False
                try:
                    current = large_data[next_key]
                except KeyError:
                    return False
            return True
        except Exception:
            return all(key in data_dict)
if __name__ == '__main__':
    verifier = ScalableKeyVerifier()
    sample_large_dataset_1 = {
        "level1": {"level2": {"target_key": 42, "other_data": [1, 2, 3]}},
        "irrelevant": "data"
    }
    sample_large_dataset_2 = {
        "nested": {"deeply_nested": {"target_key": None}},
        "missing_target": True
    }
    target_keys_to_verify = ["level1", "level2"]
    result_batch = verifier.batch_verify([sample_large_dataset_1, sample_large_dataset_2], "target_key")
    print(result_batch)