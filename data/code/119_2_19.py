from typing import Any

def reverse_order(a: Any, b: Any) -> tuple:
    return (b, a)

if __name__ == '__main__':
    result = reverse_order(10, "hello")
    print(result)