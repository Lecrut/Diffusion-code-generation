from typing import Any, Union
def is_strictly_greater(a: Any, b: Any) -> bool:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return False
    try:
        a_num = float(a)
        b_num = float(b)
        return a_num > b_num
    except ValueError:
        return False
if __name__ == '__main__':
    print(is_strictly_greater(10, 5))