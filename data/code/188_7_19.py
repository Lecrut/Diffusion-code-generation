from typing import List, Any
REVERSE_SLICE = slice(None, None, -1)

def reverse_list_strict(input_list: List[Any]) -> List[Any]:
    return input_list[REVERSE_SLICE]
if __name__ == '__main__':
    sample_values = [1, 2, 3, 'a', 'b', 'c']
    reversed_sample = reverse_list_strict(sample_values)
    print(reversed_sample)