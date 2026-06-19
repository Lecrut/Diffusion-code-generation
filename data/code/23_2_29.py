def compare_sums_and_lists(list_a, list_b):
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    difference_in_sums = sum_a - sum_b
    absolute_difference_in_lists = abs(len(list_a) - len(list_b))
    return difference_in_sums, absolute_difference_in_lists

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [6, 7, 8]
    result = compare_sums_and_lists(list_a, list_b)
    print(result)