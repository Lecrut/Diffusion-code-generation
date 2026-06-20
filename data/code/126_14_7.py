from typing import List

def lists_equal(list1: List, list2: List) -> bool:
    return list1 == list2
if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [1, 2, 3]
    print(lists_equal(sample_list1, sample_list2))