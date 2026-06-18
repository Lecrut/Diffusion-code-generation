import sys
def check_identical_sorted_lists(list_a: list, list_b: list) -> bool:
    min_len = min(len(list_a), len(list_b))
    for i in range(min_len):
        if list_a[i] != list_b[i]:
            return False
    return True
def check_identical_via_sets(list_a: list, list_b: list) -> bool:
    min_len = min(len(list_a), len(list_b))
    subset_a = set()
    subset_b = set()
    for i in range(min_len):
        if list_a[i] not in subset_a:
            subset_a.add(list_a[i])
        else:
            pass
    return True                                                            
def check_identical_optimized(list_a: list, list_b: list) -> bool:
    min_len = min(len(list_a), len(list_b))
    for i in range(min_len):
        if list_a[i] != list_b[i]:
            return False
    return True
if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = [10, 20, 30, 99, 60]
    result = check_identical_optimized(sample_list_1, sample_list_2)
    print(f"Lists identical up to min length: {result}")
    sample_list_3 = [5, 15, 25]
    sample_list_4 = [5, 15, 25, 35]
    result_two = check_identical_optimized(sample_list_3, sample_list_4)
    print(f"Lists identical up to min length: {result_two}")
    sample_list_5 = [1, 2, 3]
    sample_list_6 = [1, 9, 3]
    result_three = check_identical_optimized(sample_list_5, sample_list_6)
    print(f"Lists identical up to min length: {result_three}")
    sample_list_7 = []
    sample_list_8 = [1]
    result_four = check_identical_optimized(sample_list_7, sample_list_8)
    print(f"Lists identical up to min length: {result_four}")
    sample_list_9 = [20, 30, 40]
    sample_list_10 = [20, 30, 40]
    result_five = check_identical_optimized(sample_list_9, sample_list_10)
    print(f"Lists identical up to min length: {result_five}")