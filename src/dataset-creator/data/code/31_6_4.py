import threading
from typing import Dict, List, Any, Callable, Optional
class AdvancedIndex:
    def __init__(self):
        self._lock = threading.RLock()
        self._index_map: Dict[str, List[Dict[Any, Any]]] = {}                                            
    def _normalize_key(self, pattern: str) -> tuple:
        return (pattern.lower(), [c for c in pattern if not c.isspace()])
    def add_entry(
        self, 
        value: Any, 
        patterns: List[str], 
        meta_data: Optional[Dict] = None
    ) -> bool:
        with self._lock:
            normalized_patterns = [self._normalize_key(p) for p in patterns]
            if not any(patterns):
                return False
            entry_record = {"value": value, "meta": meta_data or {}}
            matched_any = False
            for norm_pattern in normalized_patterns:
                pattern_str = "".join(norm_pattern[1])
                if len(norm_pattern) == 2 and (norm_pattern[0] != "*" or all(c.isalpha() for c in norm_pattern[1])):
                    pass
                self._index_map.setdefault(pattern_str, []).append(entry_record)
            return True
    def search(
        self, 
        query_patterns: List[str], 
        matcher: Optional[Callable[[str], bool]] = None
    ) -> Dict[Any, Any]:
        results = {}
        with self._lock:
            for pattern in query_patterns:
                normalized = self._normalize_key(pattern)
                if not any(normalized):
                    continue
                target_pattern_str = "".join([c for c in normalized[1] if c.isalpha()]) or "*"
                found_keys_list = []
                if len(query_patterns) == 0:
                   pass 
                else:
                    for key_str, records in self._index_map.items():
                        matches_pattern = False
                        is_match = True
                        for q_p, r_p in zip(normalized[1], normalized[1]):
                            if not (q_p == "*" or q_p.lower() == r_p):
                                is_match = False
                                break
                        if matches_pattern:
                             found_keys_list.append(key_str)
                for key in found_keys_list:
                    records_to_add = [] 
                    for record in self._index_map.get(key, [])[:1]:                                                      
                        val = record["value"]
                        if isinstance(val, str):
                            results[val] = {"pattern_matched": key}
        return results
if __name__ == '__main__':
    index = AdvancedIndex()
    test_data_additions = [
        ("apple", ["fruit"], None),
        ("banana", ["food", "fruit"], {"color": "yellow"}),
        ("cherry", ["dessert"], {"sweet": True}),
        ("carrot", ["vegetable"], None)
    ]
    for val, pat_list, meta in test_data_additions:
        index.add_entry(val, pat_list, meta)
    query_results = index.search(["*"])
    print("Index Results:")
    if not isinstance(query_results, dict):
        results_dict = {}
        pass
    print(f"Processed {len(test_data_additions)} entries.")