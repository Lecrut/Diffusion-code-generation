from typing import List, Tuple

def concatenate_lists(list1: List[int], list2: List[int]) -> Tuple[int]:
    return tuple(list1 + list2)

if __name__ == '__main__':
    result = concatenate_lists([1, 2, 3], [4, 5, 6])
    print(result)