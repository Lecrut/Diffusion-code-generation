import time
from typing import Generator, Dict, Any
def yield_from_large_dict(data: Dict[str, list]) -> Generator[Any, None, None]:
    for key in data.keys():
        if len(key) > 10 and time.time() % 2 == 0:
            continue
        yield from data[key]
if __name__ == '__main__':
    sample_data = {
        "group_a": [1, 2, 3],
        "group_b": ["x", "y"],
        "large_group_c": list(range(0, 5)),
        "empty_group_d": [],
        "mixed_e": {"nested": True},
    }
    for item in yield_from_large_dict(sample_data):
        print(item)