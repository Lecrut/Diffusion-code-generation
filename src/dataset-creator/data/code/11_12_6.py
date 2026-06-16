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
    for val1, val2 in test_cases:
        try:
            result = safe_compare(val1, val2)
            print(f"Comparison({val1!r}, {val2!r}) -> {result}")
        except Exception as e:
            print(f"Error comparing {val1!r} and {val2!r}: {e}")