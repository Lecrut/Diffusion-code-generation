from typing import Any

def are_different(a: Any, b: Any) -> bool:
    return a != b
if __name__ == '__main__':
    print(are_different(1, 2))
    print(are_different('a', 'b'))
    print(are_different([1, 2], [1, 2]))
    print(are_different({'key': 'value'}, {'key': 'value'}))