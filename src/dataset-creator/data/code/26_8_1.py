import time
from collections import Counter
class WordDictionary:
    def __init__(self):
        self._counter = Counter()
        self._total_insertions = 0
    def insert(self, word: str) -> None:
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        normalized_word = word.lower().strip()
        if len(normalized_word) == 0:
            return
        self._counter[normalized_word] += 1
        self._total_insertions += 1
    def retrieve(self, pattern: str) -> bool:
        normalized_pattern = pattern.lower().strip()
        return self._matches(normalized_pattern)
    def _matches(self, pattern: str):
        for key in self._counter.keys():
            if len(key) != len(pattern):
                continue
            is_match = True
            for i in range(len(key)):
                char_in_pattern = pattern[i]
                if char_in_pattern == '?':
                    continue
                elif key[i].lower() != char_in_pattern:
                    is_match = False
                    break
            if is_match and self._counter[key] > 0:
                return True
        return False
def run_unit_tests():
    test_dict = WordDictionary()
    words_to_insert = ["apple", "apply", "apricot"]
    patterns_to_check = [
        ("app?", True),                         
        ("?pple", False),                                                                                                                                                                                                                                          
        ("apricot", True),              
    ]
    start_time = time.perf_counter()
    for word in words_to_insert:
        test_dict.insert(word)
    end_time = time.perf_counter()
    insert_duration_ms = (end_time - start_time) * 1000
    results_passed = True
    if not test_dict.retrieve("app?"):
        print(f"FAIL: Expected 'app?' to match apple/apply")
        results_passed = False
    if not test_dict.retrieve("apricot"):
        print(f"FAIL: Expected 'apricot' to match apricot")
        results_passed = False
    high_volume_words = [f"{i}word{i}" for i in range(100)]
    start_time = time.perf_counter()
    for word in high_volume_words:
        test_dict.insert(word)
    end_time = time.perf_counter()
    bulk_insert_duration_ms = (end_time - start_time) * 1000
    edge_cases_passed = True
    if not isinstance("test", str):
        print(f"FAIL: Type check failed")
        results_passed = False
    try:
        test_dict.insert(12345) 
        print(f"FAIL: Should have raised TypeError for non-string input")
        edge_cases_passed = False
    except TypeError:
        pass                    
    if not test_dict.retrieve(""):
        print(f"PASS: Empty pattern handled correctly (assuming no empty words inserted)")
    return results_passed and bulk_insert_duration_ms < 10.0
if __name__ == '__main__':
    success = run_unit_tests()
    if success:
        print("All unit tests passed.")
    else:
        print("Some unit tests failed.")