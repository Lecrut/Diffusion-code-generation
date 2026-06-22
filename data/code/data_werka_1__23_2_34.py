def compare_sums_and_lists(list_a, list_b):
    sum_a = sum(list_a)
    sum_b = sum(list_b)
    difference_in_sums = abs(sum_a - sum_b)
    if len(list_a) != len(list_b):
        raise ValueError('Lists must be of the same length')
    list_difference = [abs(a - b) for a, b in zip(list_a, list_b)]
    total_list_difference = sum(list_difference)
    return (difference_in_sums, total_list_difference)
if __name__ == '__main__':
    list_a = [1, 2, 3, 4]
    list_b = [4, 5, 6, 7]
    result = compare_sums_and_lists(list_a, list_b)
    print(result)