from typing import List

def merge_lists(list1: List[int], list2: List[int]) -> List[int]:
    return [item for sublist in (list1, list2) for item in sublist]

if __name__ == '__main__':
    sample_list_x = [7, 8, 9]
    sample_list_y = [10, 11, 12]
    combined_list = merge_lists(sample_list_x, sample_list_y)
    print(combined_list)