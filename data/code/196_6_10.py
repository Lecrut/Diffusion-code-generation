from typing import List, Tuple

def concatenate_lists(list1: List[int], list2: List[int]) -> Tuple[List[int]]:
    if not all(isinstance(item, int) for item in list1 + list2):
        raise ValueError("Both lists must contain only integers")
    
    result = list1 + list2
    return tuple(result)

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    result = concatenate_lists(list_a, list_b)
    print(result)