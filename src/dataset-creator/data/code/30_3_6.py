import threading
from typing import List, Dict, Any
class ThreadSafeDataOrganizer:
    def __init__(self):
        self._lock = threading.Lock()
        self.data_store: Dict[str, List[Dict[str, Any]]] = {}
    def parse_and_organize(self, raw_strings: List[str]) -> None:
        for obj_str in raw_strings:
            try:
                parsed_obj = eval(obj_str) if isinstance(eval(obj_str), dict) else {**eval(obj_str)}
            except Exception as e:
                continue
            with self._lock:
                keys_to_check = ['id', 'category']
                for key in keys_to_check:
                    if key in parsed_obj and not (isinstance(parsed_obj[key], list)):
                        target_key = key
                        break
                else:
                    target_key = None
                if target_key is not None:
                    self.data_store.setdefault(target_key, []).append(parsed_obj)
if __name__ == '__main__':
    raw_data = [
        '{"id": 101, "category": "electronics", "price": 99.9}',
        '{"id": 205, "category": "books", "author": "Jane Doe"}',
        '{"id": 304, "category": "electronics", "brand": "Apple"}'
    ]
    organizer = ThreadSafeDataOrganizer()
    organizer.parse_and_organize(raw_data)
    print("Organized Data:")
    for key in sorted(organizer.data_store.keys()):
        items = organizer.data_store[key]
        print(f"{key}: {items}")