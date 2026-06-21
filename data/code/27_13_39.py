from typing import Any

def are_different(a: Any, b: Any) -> bool:
    return not a == b

if __name__ == '__main__':
    print(are_different(5, 10))
    print(are_different('hello', 'world'))
    print(are_different([1, 2], [3, 4]))
    print(are_different(7.5, 7.5))
    print(are_different(True, False))