from typing import Any

def are_different(a: Any, b: Any) -> bool:
    return a != b
if __name__ == '__main__':
    print(are_different(10, 20))
    print(are_different('hello', 'world'))
    print(are_different(3.14, 3.14))
    print(are_different(True, False))
    print(are_different([1, 2], [1, 2]))