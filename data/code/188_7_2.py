from typing import List

def reverse_list_strict(input_list: List[Any]) -> List[Any]:
    return input_list[::-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 'a', 'b', 'c']
    reversed_list = reverse_list_strict(sample_list)
    print(reversed_list)