from typing import Any

def reverse_order(a: Any, b: Any) -> tuple:
    return (b, a)

if __name__ == '__main__':
    value_x = 78
    value_y = 34
    result = reverse_order(value_x, value_y)
    print(result)