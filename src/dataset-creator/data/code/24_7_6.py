import time
from typing import Iterator, Dict, Any
def create_generator(data: Dict[str, list]) -> Iterator[Any]:
    for key in data.keys():
        if isinstance(data[key], list):
            yield from data[key]
        else:
            yield data[key]
if __name__ == '__main__':
    sample_data = {
        "group_a": [1, 2, 3, 4, 5],
        "group_b": ["apple", "banana", "cherry"],
        "single_item": {"id": 99},
        "empty_group": []
    }
    gen = create_generator(sample_data)
    start_time = time.time()
    for item in gen:
        print(item, end=" ")
    end_time = time.time()
    print(f"\nTotal items yielded and printed successfully.")