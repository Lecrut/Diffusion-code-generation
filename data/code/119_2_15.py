from typing import Any

def reverse_order(a: Any, b: Any) -> tuple:
    if not all(isinstance(i, (int, str)) for i in [a, b]):
        raise ValueError("Both arguments must be either integers or strings.")
    return (b, a)

if __name__ == '__main__':
    result1 = reverse_order(42, 24)
    print(result1)
    result2 = reverse_order('hello', 'world')
    print(result2)