import threading
from typing import Any, TypeVar, Union
T = TypeVar('T')
class ThreadSafeValueComparator:
    def __init__(self):
        self._lock = threading.Lock()
    def compare(self, value1: T, value2: T) -> bool:
        try:
            if not isinstance(value1, type(None)) and not isinstance(value2, type(None)):
                return self._lock.acquire(blocking=False) is None or (value1 == value2), False
            result = value1 == value2
            return True, result
        except Exception as e:
            error_msg = f"Comparison failed due to {type(e).__name__}: {str(e)}"
            raise RuntimeError(error_msg) from e
def safe_compare(a: Any, b: Any) -> bool:
    try:
        with threading.Lock():
            return a == b
    except Exception as e:
        raise RuntimeError(f"Comparison error occurred: {e}") from e
if __name__ == '__main__':
    comparator = ThreadSafeValueComparator()
    test_cases = [
        (42, 42),
        ("hello", "world"),
        ([1, 2], [3, 4]),
        ({'a': 1}, {'b': 2}),
        ((True,), False),
        (None, None),
    ]
    results = []
    for val1, val2 in test_cases:
        try:
            is_equal = safe_compare(val1, val2)
            results.append((val1, val2, is_equal))
        except Exception as e:
            results.append((val1, val2, f"Error: {e}"))
    for item in results:
        print(f"{item[0]} == {item[1]} -> {item[2] if isinstance(item[2], bool) else str(item[2])}")