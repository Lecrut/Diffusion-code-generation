from typing import List, Any

def reverse_list_strict(input_list: List[Any]) -> List[Any]:
    return input_list[::-1]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 'a', 'b', 'c']
    reversed_values = reverse_list_strict(sample_values)
    print(reversed_values)