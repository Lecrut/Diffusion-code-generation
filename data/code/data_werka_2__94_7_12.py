def contains_truthy(iterable):
    truthy_count = sum(1 for value in iterable if value)
    return truthy_count > 0

if __name__ == '__main__':
    sample_list_positive = [False, False, True]
    sample_list_negative = [False, False, False]
    sample_list_zeros = [0, 0, 0]
    sample_list_nones = [None, None, None]
    sample_list_empty = []

    result_pos = contains_truthy(sample_list_positive)
    result_neg = contains_truthy(sample_list_negative)
    result_zeros = contains_truthy(sample_list_zeros)
    result_nones = contains_truthy(sample_list_nones)
    result_empty = contains_truthy(sample_list_empty)

    print(result_pos)
    print(result_neg)
    print(result_zeros)
    print(result_nones)
    print(result_empty)