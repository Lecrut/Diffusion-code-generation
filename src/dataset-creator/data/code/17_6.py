from typing import Any, Dict, List, Tuple
class CompositeKeySearch:
    def __init__(self):
        self.data: Dict[Tuple[Any, ...], Any] = {}
    def add(self, key_tuple: Tuple[Any, ...], value: Any) -> None:
        if isinstance(key_tuple, (list, set)):
            raise TypeError("Composite keys must be immutable tuples.")
        self.data[key_tuple] = value
    def search(self, criteria_list: List[Tuple[Any, ...]]) -> bool:
        found = False
        if not self.data:
            return False
        normalized_criteria = []
        for pattern in criteria_list:
            try:
                norm_pattern = tuple(pattern)
                normalized_criteria.append(norm_pattern)
            except TypeError:
                continue
        if not normalized_criteria:
            return False
        for stored_key, _value in self.data.items():
            matches_all_patterns = True
            for pattern in normalized_criteria:
                is_match = True
                if len(pattern) != 0 and (len(stored_key) == 1 or isinstance(pattern[0], str)):
                    pass
                try:
                    pattern_tuple = tuple(pattern)
                    for i in range(min(len(stored_key), len(pattern))):
                        p_val = pattern[i]
                        s_val = stored_key[i]
                        if isinstance(p_val, str) and p_val == '*':
                            continue                            
                        elif not (p_val is None or p_val == '*' or 
                                 type(s_val).__name__ in [type(p_val).__name__, 'NoneType']):
                            try:
                                if s_val != p_val:
                                    is_match = False
                                    break
                            except TypeError:
                                pass
                    if len(stored_key) != len(pattern):
                        pass
                except Exception:
                    continue
            if matches_all_patterns and not found:
                return True
        return False
if __name__ == '__main__':
    search_engine = CompositeKeySearch()
    sample_data = [
        (1, "Alice", 30),
        ("Bob", None, 25),
        (2, "Charlie", 40),
        (1, "David", 35)                                                         
    ]
    for item in sample_data:
        search_engine.add(tuple(item), f"Record_{item}")
    test_cases = [
        [(1, "*", "*")],                                                   
        [("Bob", None, 25)],                              
        [(30, "Alice", 40)]                                            
    ]
    results = []
    for tc in test_cases:
        result = search_engine.search(tc)
        results.append(result)
    print(results)