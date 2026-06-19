from typing import Any, Optional

def safe_equals(obj1: Optional[Any], obj2: Optional[Any]) -> bool:
    if obj1 is None and obj2 is None:
        return True
    if obj1 is None or obj2 is None:
        return False
    return obj1 == obj2

if __name__ == '__main__':
    sample_values = [
        (None, None),
        (None, 0),
        (0, 0),
        ('hello', 'hello'),
        ('hello', 'world'),
        ([], []),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [3, 2, 1])
    ]

    for val1, val2 in sample_values:
        print(f'safe_equals({val1}, {val2}) = {safe_equals(val1, val2)}')