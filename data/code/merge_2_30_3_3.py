import threading
from typing import List, Dict, Any
class DataProcessor:
    def __init__(self):
        self._lock = threading.Lock()
        self.id_groups: Dict[str, List[Dict]] = {}
        self.category_groups: Dict[str, List[Dict]] = {}
    def parse_objects(self, raw_strings: List[str]) -> None:
        parsed_data = []
        for obj_str in raw_strings:
            try:
                data = eval(obj_str)                                                                   
                if isinstance(data, dict):
                    parsed_data.append(data)
                else:
                    raise ValueError(f"Invalid object structure for {obj_str}")
            except Exception as e:
                print(f"Error parsing '{obj_str}': {e}")
        with self._lock:
            self.id_groups = {}
            self.category_groups = {}
            for item in parsed_data:
                obj_id = str(item.get('id', 'unknown'))
                category = str(item.get('category', 'uncategorized'))
                if obj_id not in self.id_groups:
                    self.id_groups[obj_id] = []
                if category not in self.category_groups:
                    self.category_groups[category] = []
                self.id_groups[obj_id].append(item)
                self.category_groups[category].append(item)
if __name__ == '__main__':
    raw_input_list = [
        "{'id': 1, 'name': 'Alice', 'category': 'Tech'}",
        "{'id': 2, 'name': 'Bob', 'category': 'Design'}",
        "{'id': 3, 'name': 'Charlie', 'category': 'Tech'}"
    ]
    processor = DataProcessor()
    processor.parse_objects(raw_input_list)
    print("Organized by ID:")
    for k in sorted(processor.id_groups.keys()):
        print(f"{k}: {processor.id_groups[k]}")
    print("\nOrganized by Category:")
    for k in sorted(processor.category_groups.keys()):
        print(f"{k}: {processor.category_groups[k]}")