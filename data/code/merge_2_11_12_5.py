import threading
from typing import Any, Callable, TypeVar, Union
T = TypeVar('T')
class ThreadSafeComparator:
    def __init__(self):
        self._lock = threading.Lock()
    def compare(self, value1: T, value2: T) -> bool:
        with self._lock:
            try:
                return value1 == value2
            except Exception as e:
                raise RuntimeError(f"Comparison failed due to error: {e}") from None
def safe_compare(a: Any, b: Any) -> Union[bool, str]:
    try:
        result = a == b
        return bool(result) if isinstance(result, bool) else "Comparison returned non-boolean type"
    except TypeError as e:
        return f"Incompatible types or unhashable comparison error: {str(e)}"
if __name__ == '__main__':
    comparator = ThreadSafeComparator()
    test_cases = [
        (42, 42),
        ("hello", "world"),
        ([1, 2], [3, 4]),
        ({'a': 1}, {'b': 2}),
        ((True, False), (False, True)),
    ]
    for val_a, val_b in test_cases:
        result = comparator.compare(val_a, val_b)
        print(f"Comparing {val_a} and {val_b}: {result}")