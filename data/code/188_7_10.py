from typing import List, Any

def reverse_list_strict(input_list: List[Any]) -> List[Any]:
    return input_list[::-1]

if __name__ == '__main__':
    sample_list = [True, False, 'hello', 42, 3.14]
    reversed_list = reverse_list_strict(sample_list)
    print(reversed_list)