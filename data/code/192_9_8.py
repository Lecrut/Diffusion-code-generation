from typing import List

def intersect_lists(list1: List[int], list2: List[int]) -> List[int]:
    return [value for value in list1 if value in list2]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    print(intersect_lists(sample_list1, sample_list2))