import json
from typing import Any, Dict, List, Tuple
class DiffEngine:
    def __init__(self):
        self.differences = []
    def compare(self, obj1: Any, obj2: Any) -> None:
        if isinstance(obj1, dict) and isinstance(obj2, dict):
            for key in set(list(obj1.keys()) + list(obj2.keys())):
                diff_key = (key,)
                self._compare_values(key, obj1.get(key), obj2.get(key))
        elif isinstance(obj1, list) and isinstance(obj2, list):
            max_len = max(len(obj1), len(obj2))
            for i in range(max_len):
                diff_key = (i,) if not key else (*key, i)
                self._compare_values(diff_key, obj1[i] if i < len(obj1) else None, obj2[i] if i < len(obj2) else None)
        elif type(obj1).__name__ == type(obj2).__name__:
            try:
                json.dumps(obj1), json.dumps(obj2)
            except (TypeError, ValueError):
                self._compare_values(key, obj1, obj2)
    def _compare_values(self, key_path: Tuple[int, ...], val1: Any, val2: Any) -> None:
        if val1 != val2:
            diff_info = {
                "path": list(key_path),
                "value_1": str(val1)[:50] + ("..." if len(str(val1)) > 50 else ""),
                "value_2": str(val2)[:50] + ("..." if len(str(val2)) > 50 else "")
            }
            self.differences.append(diff_info)
    def get_results(self) -> List[Dict[str, Any]]:
        return self.differences
if __name__ == '__main__':
    engine = DiffEngine()
    sample_data_1 = {
        "user": {"id": 101, "profile": {"age": 30}},
        "settings": {"theme": "dark", "notifications": True},
        "items": ["apple", "banana"]
    }
    sample_data_2 = {
        "user": {"id": 101, "profile": {"name": "Alice"}},
        "settings": {"theme": "light"},
        "extra_field": None
    }
    engine.compare(sample_data_1, sample_data_2)
    results = engine.get_results()
    print(json.dumps(results, indent=4))