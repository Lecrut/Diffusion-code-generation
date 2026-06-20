from typing import Any

def check_equality(a: Any, b: Any) -> bool:
    return a == b

if __name__ == '__main__':
    print(check_equality(5, 5))
    print(check_equality("hello", "hello"))
    print(check_equality([1, 2], [1, 2]))