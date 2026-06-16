import sys
def check_identical_up_to_min_length(list_a: list, list_b: list) -> bool:
    min_len = min(len(list_a), len(list_b))
    for i in range(min_len):
        if list_a[i] != list_b[i]:
            return False
    return True
def check_identical_via_sets(list_a: list, list_b: list) -> bool:
    min_len = min(len(list_a), len(list_b))
    try:
        slice_a = set(list_a[:min_len])
        slice_b = set(list_b[:min_len])
        if not (slice_a == slice_b):
            return False
        subset_a = list_a[:min_len]
        subset_b = list_b[:min_len]
        for i in range(min(len(subset_a), len(subset_b))):
            if subset_a[i] != subset_b[i]:
                return False
    except Exception:
        return False
    return True
def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 6, 7]
    result_method1 = check_identical_up_to_min_length(list1, list2)
    result_method2 = check_identical_via_sets(list1, list2)
    print(f"Method 1 (Direct Comparison): {result_method1}")
    print(f"Method 2 (Set-based Check): {result_method2}")
if __name__ == '__main__':
    main()