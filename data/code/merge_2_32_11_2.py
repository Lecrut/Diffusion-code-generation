from collections import Counter
from typing import Any, Dict
def count_frequency_elements(collection: list) -> Dict[Any, int]:
    return Counter(collection)
if __name__ == '__main__':
    sample_data = [5, 'apple', 5.0, 'banana', 'apple', None, 'cherry']
    result = count_frequency_elements(sample_data)
    print(result)