import threading
from typing import List, Dict, Any
class ThreadSafeDataOrganizer:
    def __init__(self):
        self._lock = threading.Lock()
        self.data_store: Dict[str, List[Dict[str, Any]]] = {}
    def parse_and_organize(self, raw_strings: List[str], target_keys: List[str]) -> None:
        parsed_data = []
        for s in raw_strings:
            try:
                obj_dict = eval(s) if isinstance(eval(s), dict) else {**eval(s)}
                parsed_data.append(obj_dict)
            except Exception as e:
                print(f"Error parsing string '{s}': {e}")
        with self._lock:
            for key in target_keys:
                items = [item for item in parsed_data if isinstance(item, dict)]
                filtered_items = []
                for item in items:
                    try:
                        val = item.get(key)
                        if val is not None and str(val).strip():
                            filtered_items.append({**item})
                            break
                    except Exception as e:
                        print(f"Error accessing key '{key}' in {items}: {e}")
                self.data_store[key] = filtered_items
if __name__ == '__main__':
    organizer = ThreadSafeDataOrganizer()
    sample_strings = [
        "{'id': 1, 'category': 'electronics', 'name': 'Laptop'}",
        "{'id': 2, 'category': 'clothing', 'name': 'Shirt'}",
        "{'id': 3, 'category': 'electronics', 'name': 'Phone'}"
    ]
    organizer.parse_and_organize(sample_strings, ['id', 'category'])
    print("Organized Data:")
    for key in organizer.data_store:
        print(f"{key}: {organizer.data_store[key]}")