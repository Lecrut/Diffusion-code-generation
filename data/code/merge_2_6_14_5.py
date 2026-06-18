import operator as op
from functools import wraps
def safe_gt(a: float | int, b: float | int) -> bool:
    try:
        return op.gt(a, b)
    except TypeError:
        raise ValueError("Both arguments must be numeric.") from None
if __name__ == '__main__':
    result1 = safe_gt(5.0, 3.0)
    print(f"Result (floats): {result1}")
    try:
        result2 = safe_gt("a", "b")
    except ValueError as e:
        print(f"Error caught for strings: {e}")
    result3 = safe_gt(7, 4.5)
    print(f"Result (mixed): {result3}")