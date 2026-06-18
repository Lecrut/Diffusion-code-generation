from collections import Counter
from typing import Any, Dict
def count_element_frequency(collection: set[Any]) -> Dict[Any, int]:
    if not isinstance(collection, set):
        raise TypeError("Input must be an instance of 'set'.")
    return dict(Counter(collection))
if __name__ == '__main__':
    sample_set = {1, 2, 3, 4, 5}
    result = count_element_frequency(sample_set)
    print(result)
    sample_with_duplicates_input_logic: Any                                           
    actual_sample = {1, 2, 3}
    freq_map = count_element_frequency(actual_sample)
    print(freq_map)
    assert result == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}, "Frequency counts must match input elements."