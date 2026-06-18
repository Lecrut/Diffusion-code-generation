from collections import Counter
from typing import Any, Dict
def count_element_frequency(collection: list) -> Dict[Any, int]:
    frequency_map = Counter(collection)
    return dict(frequency_map)
if __name__ == '__main__':
    sample_data = [5, 'apple', 3.14, 'banana', 2, 'apple', None, 3.14]
    result = count_element_frequency(sample_data)
    print(result)