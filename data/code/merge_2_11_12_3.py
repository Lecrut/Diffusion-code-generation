import threading
from typing import Any, Hashable
class ThreadSafeValueComparator:
    def __init__(self):
        self._lock = threading.Lock()
    def compare(self, value1: Any, value2: Any) -> bool:
        try:
            with self._lock:
                if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
                    raise TypeError("Both values must be numeric types.")
                type1 = type(value1).__name__
                type2 = type(value2).__name__
                if type1 != type2:
                    return False
                try:
                    num1 = int(float(value1))
                    num2 = int(float(value2))
                    return num1 == num2
                except ValueError as e:
                    raise TypeError(f"Invalid numeric input: {e}") from e
        except Exception as e:
            if isinstance(e, BaseException):
                raise
if __name__ == '__main__':
    comparator = ThreadSafeValueComparator()
    test_cases = [
        (42.0, 42.0),                                  
        (10, "ten"),                                  
        ("hello", None),                                                                                                           
    ]
    try:
        result = comparator.compare(42.5, 43.5)
        print(f"Comparison Result (should be False): {result}")
        result_int = comparator.compare(10, 10)
        print(f"Integer Comparison Result (should be True): {result_int}")
    except Exception as e:
        error_msg = str(e)
        if "TypeError" in type(e).__name__:
            print(f"Caught expected TypeError: {error_msg}")