def compare_sums_and_lists(list_a, list_b):
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    difference_of_sums = sum_a - sum_b
    abs_diff_list = [abs(a - b) for a, b in zip(list_a, list_b)]
    return (difference_of_sums, abs_diff_list)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [4, 5, 6, 7]
    result = compare_sums_and_lists(list_a, list_b)
    print(result)