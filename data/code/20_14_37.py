from typing import Any

def safe_equals(obj1: Any, obj2: Any) -> bool:
    if obj1 is None and obj2 is None:
        return True
    if obj1 is None or obj2 is None:
        return False
    return obj1 == obj2
if __name__ == '__main__':
    a = {'key': 'value'}
    b = {'key': 'value'}
    c = None
    d = None
    e = {'key': 'different'}
    print(safe_equals(a, b))
    print(safe_equals(c, d))
    print(safe_equals(a, c))
    print(safe_equals(e, a))