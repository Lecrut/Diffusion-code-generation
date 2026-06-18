import threading
from typing import List, Dict, Any
class DataParser:
    def __init__(self):
        self._lock = threading.Lock()
    def parse_objects(self, raw_strings: List[str]) -> List[Dict[str, Any]]:
        parsed_data = []
        for obj_str in raw_strings:
            try:
                data_dict = eval(obj_str) if isinstance(eval(obj_str), dict) else {}
                with self._lock:
                    parsed_data.append(data_dict)
            except Exception as e:
                print(f"Error parsing object: {e}")
        return parsed_data
    def organize_by_key(self, data_list: List[Dict[str, Any]], key_name: str = 'id') -> Dict[Any, List[Dict[str, Any]]]:
        organized_map = {}
        with self._lock:
            for item in data_list:
                if isinstance(item, dict) and key_name in item:
                    value = item[key_name]
                    if value not in organized_map:
                        organized_map[value] = []
                    organized_map[value].append(item)
                elif isinstance(item, list):
                    for sub_item in item:
                        if isinstance(sub_item, dict) and key_name in sub_item:
                            value = sub_item[key_name]
                            if value not in organized_map:
                                organized_map[value] = []
                            organized_map[value].append(sub_item)
        return organized_map
if __name__ == '__main__':
    parser = DataParser()
    sample_data = [
        '{"id": 1, "category": "electronics", "price": 99.99}',
        '"[{"id": 2, "category": "clothing"}, {"id": 3, "category": "shoes"}]"',
        '{"name": "Widget A", "specs": [{"model": "X100", "year": 2020}, {"model": "Y200", "year": 2021}]}'
    ]
    parsed = parser.parse_objects(sample_data)
    organized = parser.organize_by_key(parsed, key_name='id')
    print("Organized Data by ID:")
    for k, v in organized.items():
        print(f"ID {k}:")
        for item in v:
            if isinstance(item, dict):
                print(f"  - {item}")
            else:
                print(f"  - List Item: {item}")