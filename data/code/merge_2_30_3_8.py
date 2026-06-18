import threading
from typing import List, Dict, Any
class ThreadSafeOrganizer:
    def __init__(self):
        self._lock = threading.Lock()
        self.organized_data: Dict[str, List[Dict[str, Any]]] = {}
    def parse_and_organize(self, raw_strings: List[str], key_field: str) -> None:
        with self._lock:
            for item_str in raw_strings:
                try:
                    data = eval(item_str)                                                          
                    if isinstance(data, dict):
                        value = data.get(key_field)
                        if key_field not in self.organized_data or value is None:
                            continue
                        existing_list = self.organized_data[key_field]
                        if isinstance(existing_list, list):
                            existing_list.append(data)
                except Exception:
                    pass
    def get_category(self, category_id: str) -> List[Dict[str, Any]]:
        with self._lock:
            return self.organized_data.get(category_id, [])
if __name__ == '__main__':
    organizer = ThreadSafeOrganizer()
    raw_items = [
        "{'id': 101, 'category': 'electronics', 'price': 50}",
        "{'id': 102, 'category': 'clothing', 'price': 30}",
        "{'id': 103, 'category': 'electronics', 'price': 80}",
    ]
    organizer.parse_and_organize(raw_items, key_field='category')
    print("Electronics:", organizer.get_category('electronics'))
    print("Clothing:", organizer.get_category('clothing'))