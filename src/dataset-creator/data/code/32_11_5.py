from collections import Counter
from typing import Any, Dict
def count_frequency(collection: list) -> Dict[Any, int]:
    if not isinstance(collection, list):
        try:
            collection = list(collection)
        except TypeError:
            raise TypeError("Input must be a sequence that can be converted to a list.")
    return dict(Counter(collection))
if __name__ == '__main__':
    sample_data = [10, 20, 'apple', 'banana', 3.5, 'orange', 10, 20]
    result = count_frequency(sample_data)
    print(result)