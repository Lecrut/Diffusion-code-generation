from typing import List

def merge_lists(list1: List[int], list2: List[int]) -> List[int]:
    return [item for sublist in (list1, list2) for item in sublist]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3]
    sample_list2 = [4, 5, 6]
    merged_list = merge_lists(sample_list1, sample_list2)
    print(merged_list)