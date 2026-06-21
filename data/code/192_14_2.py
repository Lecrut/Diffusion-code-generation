from typing import List

def find_common_elements(list1: List[int], list2: List[int]) -> List[int]:
    return list(set(list1) & set(list2))

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    print(find_common_elements(sample_list1, sample_list2))