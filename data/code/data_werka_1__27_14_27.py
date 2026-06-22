from typing import Any

def are_different(a: Any, b: Any) -> bool:
    return a != b

if __name__ == '__main__':
    x = 42
    y = 'hello'
    print(are_different(x, y))