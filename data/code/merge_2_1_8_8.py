import sys
def check_sorted_lists_identical(list_a: list[int], list_b: list[int]) -> bool:
    min_len = min(len(list_a), len(list_b))
    for i in range(min_len):
        if list_a[i] != list_b[i]:
            return False
    return True
def check_sorted_lists_identical_set_based(list_a: list[int], list_b: list[int]) -> bool:
    min_len = min(len(list_a), len(list_b))
    slice_a = tuple(list_a[:min_len])
    slice_b = tuple(list_b[:min_len])
    return slice_a == slice_b
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4]
    sample_list_2 = [1, 2, 3, 5]
    sample_list_3 = [7, 8, 9]
    result_func1 = check_sorted_lists_identical(sample_list_1, sample_list_2)
    result_set_based = check_sorted_lists_identical_set_based(sample_list_1, sample_list_2)
    result_three_way = check_sorted_lists_identical(sample_list_3, [7, 8])
    print(f"List A vs List B (direct): {result_func1}")
    print(f"List A vs List B (set-based): {result_set_based}")
    print(f"Shorter list match: {result_three_way}")