from typing import Any, Optional

def safe_equals(obj1: Any, obj2: Any) -> bool:
    if obj1 is None and obj2 is None:
        return True
    if obj1 is None or obj2 is None:
        return False
    return obj1 == obj2
if __name__ == '__main__':
    a = None
    b = None
    c = 42
    d = 'hello'
    e = 'hello'
    print(safe_equals(a, b))
    print(safe_equals(a, c))
    print(safe_equals(d, e))
    print(safe_equals(c, d))