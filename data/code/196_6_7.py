from typing import List, Tuple

def concatenate_lists(list1: List[int], list2: List[int]) -> Tuple[List[int]]:
    combined_list = list1 + list2
    return combined_list,

if __name__ == '__main__':
    sample_list_a = [7, 8, 9]
    sample_list_b = [10, 11, 12]
    result = concatenate_lists(sample_list_a, sample_list_b)
    print(result)