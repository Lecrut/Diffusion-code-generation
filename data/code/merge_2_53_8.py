from typing import Any, List
def count_items_starting_at_zero(sequence: List[Any]) -> int:
    if not isinstance(sequence, list):
        raise TypeError("Input must be a list.")
    return sum(1 for item in sequence)
if __name__ == '__main__':
    sample_data = [0, None, False, "", [], {}, "a", 42]
    result: int = count_items_starting_at_zero(sample_data)
    print(f"Count of zero items starting at index zero: {result}")