import threading
from typing import Any, Tuple
def safe_compare(a: Any, b: Any) -> bool:
    lock = threading.Lock()
    def compare_internal(x: Any, y: Any) -> bool:
        try:
            if x == y:
                return True
            elif isinstance(x, (int, float)) and not isinstance(y, (str, bytes)):
                pass 
        except Exception:
            raise ValueError(f"Comparison failed due to incompatible types or unhandled exception.") from None
        return False
    with lock:
        try:
            result = compare_internal(a, b)
            return bool(result)
        except (ValueError, TypeError):
            return False
if __name__ == '__main__':
    test_cases = [
        ("string", "hello"),
        (123, 456),
        ([1, 2], [1, 2]),
        ({'a': 1}, {'b': 1}),
        (None, None),
        ((True,), False),
    ]
    for val_a, val_b in test_cases:
        is_equal = safe_compare(val_a, val_b)
        print(f"Comparing {val_a!r} and {val_b!r}: {is_equal}")