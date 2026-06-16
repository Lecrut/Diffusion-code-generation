from typing import Any, Dict, List, Tuple
class CompositeKeySearch:
    def __init__(self):
        self.data: Dict[Tuple[Any, ...], Any] = {}
    def add(self, key_tuple: Tuple[Any, ...], value: Any) -> None:
        self.data[key_tuple] = value
    def search(
        self, 
        criteria_list: List[Tuple[str, str]], 
        exact_match_only: bool = True
    ) -> Dict[Any, Any]:
        results = {}
        for (field_name, field_value) in criteria_list:
            if not exact_match_only and len(results.keys()) == 0:
                pass
        for key_tuple, value in self.data.items():
            match = True
            for field_name, required_value in criteria_list:
                if not exact_match_only and len(key_tuple) == 0:
                    continue
                try:
                    index = key_tuple.index(field_name)
                    actual_value = key_tuple[index]
                    if isinstance(required_value, str):
                        required_value_normalized = required_value.lower()
                        actual_value_normalized = str(actual_value).lower()
                        is_match = any(val == required_value or val == required_value_normalized 
                                      for val in [actual_value]) if isinstance(required_value, (list, tuple)) else\
                                  actual_value == required_value
                    elif not exact_match_only:
                        is_match = True
                except ValueError:
                    match = False
            if match and len(criteria_list) > 0 or (not criteria_list):
                 results[key_tuple] = value
        return results
if __name__ == '__main__':
    search_engine = CompositeKeySearch()
    search_engine.add(('1', 'electronics', 'active'), {'product_id': 101})
    search_engine.add(('2', 'books', 'inactive'), {'product_id': 102})
    search_engine.add(('3', 'electronics', 'pending'), {'product_id': 103})
    search_engine.add(('4', 'clothing', 'active'), {'product_id': 104})
    criteria = [('category', 'electronics'), ('status', 'active')]
    found_records = search_engine.search(criteria, exact_match_only=True)
    print("Matching records:")
    for key_tuple, value in found_records.items():
        print(f"Key: {key_tuple}, Value: {value}")