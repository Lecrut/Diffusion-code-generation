from typing import List, Any

def reverse_list_strict(input_list: List[Any]) -> List[Any]:
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    
    return input_list[::-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 'a', 'b', 'c']
    try:
        reversed_list = reverse_list_strict(sample_list)
        print(reversed_list)
    except ValueError as e:
        print(e)