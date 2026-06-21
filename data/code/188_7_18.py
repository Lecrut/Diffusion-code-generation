from typing import List, Any

def reverse_list_strict(input_list: List[Any]) -> List[Any]:
    return input_list[::-1]

if __name__ == '__main__':
    sample_values = [10, 20, 30, 'x', 'y', 'z']
    reversed_values = reverse_list_strict(sample_values)
    print(reversed_values)