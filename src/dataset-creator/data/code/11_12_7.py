import threading
from typing import Any, TypeVar, Union
T = TypeVar('T')
class EqualityError(Exception):
    pass
def safe_compare(a: T, b: T) -> bool:
    thread_lock = threading.Lock()
    with thread_lock:
        try:
            type_a = type(a)
            type_b = type(b)
            if type_a != type_b:
                raise EqualityError(f"Types must be identical for equality check: {type_a} vs {type_b}")
            return a == b
        except Exception as e:
            raise EqualityError(f"Comparison failed due to error: {str(e)}")
if __name__ == '__main__':
    test_cases = [
        ("Integer equality", 42, 42),
        ("Float inequality", 3.14, 3.15),
        ("String match", "hello", "world"),
        ("Type mismatch attempt (will raise error)", 10, "ten")
    ]
    for desc, val_a, val_b in test_cases:
        try:
            result = safe_compare(val_a, val_b)
            print(f"{desc}: {result}")
        except EqualityError as e:
            print(f"{desc} raised Exception: {e}")