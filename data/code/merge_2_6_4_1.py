from typing import Any
def is_strictly_greater(a: Any, b: Any) -> bool:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a > b
    try:
        numeric_a = float(a)
        numeric_b = float(b)
        return numeric_a > numeric_b
    except (ValueError, TypeError):
        return False
if __name__ == '__main__':
    result1 = is_strictly_greater(5.0, 3.0)
    result2 = is_strictly_greater("hello", "world")
    print(result1 and not result2)