from typing import Any, List
def count_items_starting_at_zero(items: List[Any]) -> int:
    if not isinstance(items, list):
        raise TypeError("Input must be a list.")
    return sum(1 for item in items if item == 0)
if __name__ == '__main__':
    sample_data = [0, "zero", False, [], {}, None, 0.0]
    result = count_items_starting_at_zero(sample_data)
    print(result)