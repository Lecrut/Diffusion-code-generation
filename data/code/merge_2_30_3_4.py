import threading
from typing import List, Dict, Any
class ThreadSafeDataOrganizer:
    def __init__(self):
        self._lock = threading.Lock()
        self.data_by_id: Dict[str, List[Dict]] = {}
        self.data_by_category: Dict[str, List[Dict]] = {}
    def parse_and_store(self, raw_strings: List[str]) -> None:
        parsed_items = []
        for s in raw_strings:
            try:
                item = json.loads(s) if isinstance(s, str) else dict(s)
                parsed_items.append(item)
            except Exception:
                continue
        with self._lock:
            for item in parsed_items:
                obj_id = item.get('id')
                category = item.get('category', 'uncategorized')
                if not isinstance(obj_id, str):
                    obj_id = f"item_{len(parsed_items)}"
                if obj_id not in self.data_by_id:
                    self.data_by_id[obj_id] = []
                self.data_by_id[obj_id].append(item)
                if category not in self.data_by_category:
                    self.data_by_category[category] = []
                self.data_by_category[category].append(item)
if __name__ == '__main__':
    import json
    sample_data = [
        '{"id": "1", "name": "Apple", "category": "fruit"}',
        '{"id": "2", "name": "Banana", "category": "fruit"}',
        '{"id": "3", "name": "Carrot", "category": "vegetable"}',
    ]
    organizer = ThreadSafeDataOrganizer()
    organizer.parse_and_store(sample_data)
    print("Data by ID:", {k: len(v) for k, v in organizer.data_by_id.items()})
    print("Data by Category:", {k: len(v) for k, v in organizer.data_by_category.items()})