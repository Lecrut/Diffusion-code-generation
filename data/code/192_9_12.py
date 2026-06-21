from typing import List

def validate_lists(list1: List[int], list2: List[int]) -> None:
    if not isinstance(list1, list) or not all(isinstance(x, int) for x in list1):
        raise ValueError("list1 must be a list of integers")
    if not isinstance(list2, list) or not all(isinstance(x, int) for x in list2):
        raise ValueError("list2 must be a list of integers")

def find_common_elements(list1: List[int], list2: List[int]) -> List[int]:
    validate_lists(list1, list2)
    return [element for element in set(list1) if element in list2]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    common_elements = find_common_elements(list1, list2)
    print(f"Common elements in {list1} and {list2}: {common_elements}")