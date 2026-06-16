import threading
from typing import Any, TypeVar
T = TypeVar('T')
class ThreadSafeEqualityChecker:
    def __init__(self):
        self._lock = threading.Lock()
    def compare(self, value1: T, value2: T) -> bool:
        try:
            with self._lock:
                return value1 == value2
        except Exception as e:
            raise RuntimeError(f"Equality comparison failed for types {type(value1)} and {type(value2)}") from e
def main():
    checker = ThreadSafeEqualityChecker()
    sample_ints = 42, 43
    sample_strings = "hello", "world"
    sample_mixed = {"key": "value"}, [1, 2, 3]
    test_cases = [
        (sample_ints[0], sample_ints[0]),
        (sample_ints[0], sample_ints[1]),
        (sample_strings[0], sample_strings[1]),
        (sample_mixed[0], None),                                                                                                                                                       
    ]
    for v1, v2 in test_cases:
        try:
            result = checker.compare(v1, v2)
            print(f"Comparison {v1} == {v2}: {result}")
        except Exception as ex:
            print(f"Error comparing {type(v1)} and {type(v2)}: {ex}")
if __name__ == '__main__':
    main()