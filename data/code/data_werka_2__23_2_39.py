def compare_sums_and_lists(list_a, list_b):
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    difference_between_sums = sum_a - sum_b
    abs_difference_between_lists = []
    for a, b in zip(list_a, list_b):
        abs_difference_between_lists.append(abs(a - b))
    return (difference_between_sums, abs_difference_between_lists)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [5, 6, 7, 8]
    result = compare_sums_and_lists(list_a, list_b)
    print(result)