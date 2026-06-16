from typing import Any, Union
def is_strictly_greater(a: Any, b: Any) -> bool:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return False
    try:
        a_val = float(a)
        b_val = float(b)
        return a_val > b_val
    except ValueError:
        return False
if __name__ == '__main__':
    result1 = is_strictly_greater(5, 3)
    print(result1)
    result2 = is_strictly_greater("a", "b")
    print(result2)
    result3 = is_strictly_greater([1], [2])
    print(result3)