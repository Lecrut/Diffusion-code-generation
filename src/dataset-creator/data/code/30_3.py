import threading
from typing import List, Dict, Any
class DataParser:
    def __init__(self):
        self._lock = threading.Lock()
        self.categorized_data: Dict[str, List[Dict[str, Any]]] = {}
    def parse_objects(self, raw_strings: List[str]) -> None:
        for obj_str in raw_strings:
            try:
                parsed_obj = eval(obj_str) if isinstance(eval(obj_str), dict) else json.loads(obj_str)
                self._categorize(parsed_obj)
            except Exception as e:
                print(f"Error parsing object: {e}")
    def _categorize(self, obj: Dict[str, Any]) -> None:
        with self._lock:
            if 'id' in obj and obj['id']:
                category = f"id_{obj['id']}"
            elif 'category' in obj and obj['category']:
                category = obj['category']
            else:
                return
            if category not in self.categorized_data:
                self.categorized_data[category] = []
            self.categorized_data[category].append(obj)
if __name__ == '__main__':
    sample_strings = [
        "{'id': 1, 'name': 'Item A', 'price': 10.5}",
        "{'id': 2, 'name': 'Item B', 'price': 20.3}",
        "{'category': 'Electronics', 'brand': 'TechCorp'}",
        "{'category': 'Clothing', 'size': 'M'}"
    ]
    parser = DataParser()
    import json
    def safe_eval(s):
        try:
            return eval(s) if isinstance(eval(s), dict) else None
        except Exception:
            return json.loads(s.replace("'", '"'))
    parser.parse_objects([safe_eval(s) for s in sample_strings])