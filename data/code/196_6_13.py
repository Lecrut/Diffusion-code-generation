from typing import List, Tuple

def concatenate_lists(list1: List[int], list2: List[int]) -> Tuple[List[int]]:
    return (list1 + list2,)

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    result = concatenate_lists(list_a, list_b)
    print(result)