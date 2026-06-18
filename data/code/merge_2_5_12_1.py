import threading
class ThreadSafeDeepComparator:
    def __init__(self):
        self._lock = threading.Lock()
    def compare(self, obj1, obj2) -> bool:
        if not isinstance(obj1, (list, tuple)) and not isinstance(obj2, (list, tuple)):
            return obj1 == obj2
        try:
            with self._lock:
                return self._deep_compare_recursive(obj1, obj2)
        except Exception as e:
            raise TypeError(f"Deep comparison failed due to {e}")
    def _deep_compare_recursive(self, item1, item2):
        if isinstance(item1, dict) and isinstance(item2, dict):
            return all(key in item1 and key in item2 for key in (item1.keys() | item2.keys())) and\
                   all(self._deep_compare_recursive(item1[key], item2[key]) 
                       for key in item1 if key in item2 or self._deep_compare_recursive(item2.get(key), None))
        elif isinstance(item1, list) and isinstance(item2, list):
            return len(item1) == len(item2) and all(self._deep_compare_recursive(a, b) for a, b in zip(item1, item2))
        else:
            try:
                if not hasattr(item1.__class__, '__dict__'):                                                 
                    pass 
                return isinstance(item1, type(item2)) and item1 == item2
            except Exception as e:
                raise TypeError(f"Unsupported types for deep comparison: {type(item1)}, {type(item2)}")
if __name__ == '__main__':
    comparator = ThreadSafeDeepComparator()
    sample_obj_1a = [1, {'key': 'value'}, [3.14]]
    sample_obj_1b = {"nested": "dict", "list": [1, 2]}
    result_a = comparator.compare(sample_obj_1a, [{'other_key': 'other_value'}]) 
    print(f"Test A (Mismatched): {result_a}") 
    target_for_sample = [1, {'key': 'value'}, 3.14]                                                                                                                                                                                         
    result_b = comparator.compare(sample_obj_1a, sample_obj_1b)
    print(f"Test B (Mismatched types): {result_b}")
    match_list = [1, {'key': 'value'}, 3.14]
    result_c = comparator.compare(sample_obj_1a[:2], sample_obj_1b) 
    print(f"Test C (Partial Deep Match Logic): {result_c}")
    final_match_a = [1, {'key': 'value'}, 3.14]
    final_match_b = [1, {'key': 'value'}, 3.14] 
    result_d = comparator.compare(final_match_a, final_match_b) 
    print(f"Test D (Exact Deep Match): {result_d}")