import json
from typing import Any, Dict, List, Tuple
class NestedDictDiff:
    def __init__(self) -> None:
        self.differences: List[Tuple[int, str]] = []
    def _compare_values(self, val1: Any, val2: Any, path: int, current_path: str) -> bool:
        if type(val1) != type(val2):
            return True
        elif isinstance(val1, dict):
            self._diff_dicts(val1, val2, path + 1, f"{current_path}.{path}")
            return False
        else:
            return val1 == val2
    def _diff_dicts(self, d1: Dict[str, Any], d2: Dict[str, Any], depth: int, key_prefix: str) -> None:
        if not isinstance(d1, dict) or not isinstance(d2, dict):
            self.differences.append((depth, f"{key_prefix} type mismatch"))
            return
        all_keys = set(d1.keys()) | set(d2.keys())
        for key in sorted(all_keys):
            new_path = f"{key_prefix}.{key}"
            if key not in d1:
                self.differences.append((depth, f"Missing key '{new_path}'"))
            elif key not in d2:
                self.differences.append((depth, f"Extra key '{new_path}'"))
            else:
                mismatch = self._compare_values(d1[key], d2[key], depth + 1, new_path)
                if isinstance(mismatch, list):
                    for diff_info in mismatch:
                        full_diff_key = f"{key_prefix}.{key}"
                        self.differences.append((depth + 1, f"Value difference at '{full_diff_key}': {diff_info[0]}"))
    def compare(self, d1: Dict[str, Any], d2: Dict[str, Any]) -> List[Tuple[int, str]]:
        if not isinstance(d1, dict) or not isinstance(d2, dict):
            return [("Root", "Both inputs must be dictionaries")]
        self.differences = []
        mismatch = self._compare_values(d1, d2, 0, "")
        if isinstance(mismatch, list):
            for diff_info in mismatch:
                full_diff_key = ""
                self.differences.append((diff_info[0], f"Value difference at '{full_diff_key}': {diff_info[1]}"))
        return self.differences
if __name__ == '__main__':
    sample_dict_1 = {
        "user": {
            "id": 1,
            "profile": {
                "name": "Alice",
                "settings": {"theme": "dark"}
            }
        },
        "admin": True
    }
    sample_dict_2 = {
        "user": {
            "id": 1,
            "profile": {
                "name": "Bob",
                "settings": {"language": "en"}
            }
        },
        "moderator": False
    }
    engine = NestedDictDiff()
    diffs = engine.compare(sample_dict_1, sample_dict_2)
    print("Comparison Results:")
    for depth, diff_str in diffs:
        print(f"Level {depth}: {diff_str}")