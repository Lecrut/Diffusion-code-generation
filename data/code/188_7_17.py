from typing import List, Any

def reverse_list_strict(input_list: List[Any]) -> List[Any]:
    return input_list[::-1]

if __name__ == '__main__':
    sample_data = ['apple', 42, True, 'banana']
    reversed_data = reverse_list_strict(sample_data)
    print(f"Original data: {sample_data}")
    print(f"Reversed data: {reversed_data}")