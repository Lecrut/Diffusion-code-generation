def compare_sums_and_lists(list_a, list_b):
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    sum_difference = sum_a - sum_b
    list_a_difference = abs(len(list_a) - len(list_b))
    list_content_difference = sum(abs(x - y) for x, y in zip(list_a, list_b))
    return sum_difference, list_content_difference, list_a_difference
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50]
    diff1, diff2, len_diff = compare_sums_and_lists(list1, list2)
    print(f"Sum difference (list1 - list2): {diff1}")
    print(f"Absolute difference in list content (element-wise sum of absolute differences): {diff2}")
    print(f"Absolute difference in list lengths: {len_diff}")