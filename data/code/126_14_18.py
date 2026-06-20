from typing import List

def are_lists_equal(list1: List[int], list2: List[int]) -> bool:
    if len(list1) != len(list2):
        return False
    for item1, item2 in zip(list1, list2):
        if item1 != item2:
            return False
    return True
if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [1, 2, 3, 4]
    print(are_lists_equal(sample_list1, sample_list2))
    sample_list3 = [1, 2, 3, 4]
    sample_list4 = [4, 3, 2, 1]
    print(are_lists_equal(sample_list3, sample_list4))