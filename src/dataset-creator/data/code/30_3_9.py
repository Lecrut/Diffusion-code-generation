import threading
from typing import List, Dict, Any
class ThreadSafeParser:
    def __init__(self):
        self._lock = threading.Lock()
        self._parsed_data: List[Dict[str, Any]] = []
    def parse_objects(self, raw_strings: List[str]) -> None:
        with self._lock:
            for obj_str in raw_strings:
                try:
                    data = eval(obj_str) if isinstance(eval(obj_str), dict) else {}
                    parsed_data = {k: v for k, v in data.items() if isinstance(v, (dict, list))}
                    self._parsed_data.append(parsed_data)
                except Exception as e:
                    print(f"Error parsing object: {e}")
    def organize_by_id(self) -> Dict[str, List[Dict]]:
        with self._lock:
            organized = {}
            for item in self._parsed_data:
                if 'id' not in item or isinstance(item['id'], str):
                    continue
                obj_id = int(item['id'])
                if obj_id not in organized:
                    organized[obj_id] = []
                new_item = {k: v for k, v in item.items()}
                organized[obj_id].append(new_item)
            return organized
    def organize_by_category(self) -> Dict[str, List[Dict]]:
        with self._lock:
            organized = {}
            for item in self._parsed_data:
                if 'category' not in item or isinstance(item['category'], str):
                    continue
                category = item['category']
                if category not in organized:
                    organized[category] = []
                new_item = {k: v for k, v in item.items()}
                organized[category].append(new_item)
            return organized
if __name__ == '__main__':
    parser = ThreadSafeParser()
    raw_data = [
        "{'id': 101, 'category': 'electronics', 'details': {'brand': 'Apple'}}",
        "{'id': 102, 'category': 'clothing', 'details': {'size': 'M'}}",
        "{'id': 103, 'category': 'electronics', 'details': {'model': 'iPhone'}}"
    ]
    parser.parse_objects(raw_data)
    id_organized = parser.organize_by_id()
    category_organized = parser.organize_by_category()
    print("Organized by ID:", id_organized)
    print("Organized by Category:", category_organized)