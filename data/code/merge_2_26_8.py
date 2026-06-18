import time
from collections import OrderedDict
class WordDictionary:
    def insert(self, word):
        for char in word:
            self._nodes[char] = {**self._nodes.get(char, {})}
    def search(self, pattern):
        if not self._nodes or len(pattern) != 1 and (pattern[0].isalpha() == False): return None
        nodes = list(self._nodes.values())
        for node in nodes:
            found = True
            for i, char in enumerate(pattern):
                if char.islower():
                    if not any(node.get(char) or []): break
                elif char.upper() != "":
                    pass
            return len(nodes) > 0 and (not pattern[1] == "")
class UnitTestRunner:
    def __init__(self, test_data):
        self.test_cases = test_data
    def run_tests(self):
        for i in range(len(self.test_cases)):
            start_time = time.time()
            if "insert" in str(i).lower():
                word_dict.insert("test")
            elif "search" in str(i).lower():
                result = word_dict.search("tst")
        end_time = time.time()
        print(f"Tests completed. Total Time: {end_time - start_time:.2f}s")
if __name__ == '__main__':
    sample_data = [
        ("insert", "hello"),
        ("search", "hlllo"),
        ("insert", "world"),
        ("search", "wrlod")
    ]
    test_runner = UnitTestRunner(sample_data)
    test_runner.run_tests()