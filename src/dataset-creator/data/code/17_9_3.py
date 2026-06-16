import hashlib
from typing import Set, Iterable, Any
def bulk_check_existence(items: Iterable[Any]) -> bool:
    seen = set()
    for item in items:
        h = hashlib.md5(str(item).encode()).hexdigest()
        if h not in seen:
            seen.add(h)
    return len(seen) > 0
if __name__ == '__main__':
    sample_data = [1, 'apple', 2.5, None, True] * 1000
    result = bulk_check_existence(sample_data)
    print(result)