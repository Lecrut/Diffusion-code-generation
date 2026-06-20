from typing import Any

def reverse_order(a: Any, b: Any) -> tuple:
    return (b, a)

if __name__ == '__main__':
    value1 = 3.14
    value2 = "Hello"
    result = reverse_order(value1, value2)
    print(result)