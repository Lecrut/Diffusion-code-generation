from collections import Counter
from typing import Any, Dict
def count_element_frequency(collection: list) -> Dict[Any, int]:
    if not isinstance(collection, list):
        raise TypeError("Input must be a list.")
    return dict(Counter(collection))
if __name__ == '__main__':
    sample_data = [5, "apple", 3.14, True, False, None, "banana"] * 2 + ["apple"]
    result = count_element_frequency(sample_data)
    print(f"Input: {sample_data}")
    print(f"Frequencies: {result}")