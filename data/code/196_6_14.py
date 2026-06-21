from typing import List, Tuple

def validate_lists(list1: List[int], list2: List[int]) -> None:
    if not all(isinstance(item, int) for item in list1):
        raise ValueError("List 1 must contain only integers")
    if not all(isinstance(item, int) for item in list2):
        raise ValueError("List 2 must contain only integers")

def concatenate_lists(list1: List[int], list2: List[int]) -> Tuple[List[int]]:
    validate_lists(list1, list2)
    return tuple(list1 + list2)

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    result = concatenate_lists(list_a, list_b)
    print(result)