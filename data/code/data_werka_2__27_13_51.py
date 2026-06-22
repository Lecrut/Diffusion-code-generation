from typing import Any

def are_different(a: Any, b: Any) -> bool:
    return not a == b
if __name__ == '__main__':
    x = [1, 2, 3]
    y = [3, 2, 1]
    z = 'hello'
    w = 'world'
    num1 = 5.0
    num2 = 5.0
    print(are_different(x, y))
    print(are_different(z, w))
    print(are_different(num1, num2))
    print(are_different(None, None))