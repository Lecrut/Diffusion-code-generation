from typing import List

def merge_lists(list1: List[int], list2: List[int]) -> List[int]:
    return [item for sublist in (list1, list2) for item in sublist]
if __name__ == '__main__':
    LIST_A = [1, 2, 3]
    LIST_B = [4, 5, 6]
    merged_list = merge_lists(LIST_A, LIST_B)
    print(merged_list)