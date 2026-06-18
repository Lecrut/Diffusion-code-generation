from typing import Any, List
def count_items_starting_at_zero(items: List[Any]) -> int:
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    counter = 0
    for item in items:
        if item == 0:
            counter += 1
    return counter
if __name__ == '__main__':
    sample_data = [0, "zero", False, [], {}, (0,), None]
    result = count_items_starting_at_zero(sample_data)
    print(f"Count of items equal to zero: {result}")