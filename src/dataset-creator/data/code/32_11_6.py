from collections import Counter
from typing import Any, Dict
def count_frequency_elements(collection: list) -> Dict[Any, int]:
    frequency_map = Counter(collection)
    return dict(frequency_map)
if __name__ == '__main__':
    sample_data = [5, 'apple', 5.0, 'banana', 'apple', None, 'cherry']
    result = count_frequency_elements(sample_data)
    print(result)