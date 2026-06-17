import threading
from typing import List, Dict, Any
class ThreadSafeParser:
    def __init__(self):
        self._lock = threading.Lock()
    def parse_objects(self, raw_strings: List[str]) -> Dict[Any, List[Dict]]:
        result_data = {}
        for obj_str in raw_strings:
            try:
                parsed_obj = eval(obj_str) if isinstance(eval(obj_str), dict) else {**eval(obj_str)}
                with self._lock:
                    id_key = 'id'
                    obj_id = parsed_obj.get(id_key, f"unnamed_{len(result_data)}")
                    if not isinstance(parsed_obj, dict):
                        continue
                    category_key = 'category'
                    cat_value = parsed_obj.get(category_key)
                    if id_key in result_data:
                        result_data[id_key].append({**parsed_obj})
                    else:
                        result_data[id_key] = [{**parsed_obj}]
            except Exception:
                continue
        return result_data
if __name__ == '__main__':
    parser = ThreadSafeParser()
    sample_strings = [
        '{"id": 1, "category": "electronics", "price": 99.99}',
        '{"id": 2, "category": "clothing", "size": "M"}',
        '{"id": 3, "category": "electronics", "brand": "Apple"}'
    ]
    organized_data = parser.parse_objects(sample_strings)
    print(organized_data)