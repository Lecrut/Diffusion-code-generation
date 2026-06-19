from typing import Any, Optional

def safe_equals(obj1: Optional[Any], obj2: Optional[Any]) -> bool:
    if obj1 is None and obj2 is None:
        return True
    if obj1 is None or obj2 is None:
        return False
    return obj1 == obj2
if __name__ == '__main__':
    print(safe_equals(None, None))
    print(safe_equals(None, 0))
    print(safe_equals(0, 0))
    print(safe_equals('a', 'a'))
    print(safe_equals('a', 'b'))