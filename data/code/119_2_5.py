from typing import Any

def reverse_order(a: Any, b: Any) -> tuple:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")
    return (b, a)

if __name__ == '__main__':
    try:
        result = reverse_order(42, 24)
        print(result)
        result = reverse_order('a', 'b')
        print(result)
    except ValueError as e:
        print(e)