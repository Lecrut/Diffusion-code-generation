from typing import List, Tuple

def concatenate_lists(list1: List[int], list2: List[int]) -> Tuple[List[int]]:
    return tuple(list1 + list2)

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    result = concatenate_lists(sample_list1, sample_list2)
    print(result)