import random
from typing import Any, Dict, Optional

def fetch_random_entry(mapping: Dict[str, Any]) -> Optional[Any]:
    keys = list(mapping)
    if not keys:
        return None
    index = random.randint(0, len(keys) - 1)
    return mapping[keys[index]]

if __name__ == '__main__':
    data = {'x': 10, 'y': 20, 'z': 30}
    empty_data = {}
    print(fetch_random_entry(data))
    print(fetch_random_entry(empty_data))