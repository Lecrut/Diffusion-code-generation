def compare_sums_and_lists(list_a, list_b):
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    difference_of_sums = sum_a - sum_b
    absolute_difference_of_lists = abs(len(list_a) - len(list_b))
    return difference_of_sums, absolute_difference_of_lists

if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [5, 6, 7]
    result = compare_sums_and_lists(list_a, list_b)
    print(result)