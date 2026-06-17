from typing import Any, List
def count_items_starting_at_zero(items: List[Any]) -> int:
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    return sum(1 for item in items if item is None)
if __name__ == '__main__':
    sample_data = [None, 0, "null", [], {}, False, None]
    result = count_items_starting_at_zero(sample_data)
    print(result)