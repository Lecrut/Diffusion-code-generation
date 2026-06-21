def compare_sums_and_lists(list_a, list_b):
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    difference_in_sums = sum_a - sum_b
    abs_difference_in_lists = 0
    for a, b in zip(list_a, list_b):
        if a != b:
            abs_difference_in_lists += 1
    abs_difference_in_lists += abs(len(list_a) - len(list_b))
    return (difference_in_sums, abs_difference_in_lists)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [2, 3, 5]
    result = compare_sums_and_lists(list_a, list_b)
    print(result)