from typing import List

def merge_lists(list1: List[int], list2: List[int]) -> List[int]:
    return [item for sublist in (list1, list2) for item in sublist]

if __name__ == '__main__':
    sample_list_x = [10, 20, 30]
    sample_list_y = [40, 50, 60]
    merged_lists = merge_lists(sample_list_x, sample_list_y)
    print(merged_lists)