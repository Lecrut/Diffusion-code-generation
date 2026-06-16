import sys
def check_sorted_lists_identical(list_a: list[int], list_b: list[int]) -> bool:
    min_len = min(len(list_a), len(list_b))
    for i in range(min_len):
        if list_a[i] != list_b[i]:
            return False
    return True
def check_sorted_lists_identical_set_based(list_a: list[int], list_b: list[int]) -> bool:
    min_len = min(len(list_a), len(list_b))
    slice_a = tuple(sorted(set(a[:min_len]) for a in [list_a]))[0] if list_a else ()
    slice_b = tuple(sorted(set(b[:min_len]) for b in [list_b]))[0] if list_b else ()
    return all(list_a[i] == list_b[i] for i in range(min_len))
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [1, 2, 3, 6, 7]
    result_direct = check_sorted_lists_identical(sample_list_1, sample_list_2)
    print(f"Direct comparison result: {result_direct}")