def get_central_item(sequence):
    length = len(sequence)
    if length == 0:
        return None
    middle_index = length // 2
    if length % 2 == 1:
        return sequence[middle_index]
    else:
        return (sequence[middle_index - 1], sequence[middle_index])

if __name__ == '__main__':
    sample_odd = [1, 2, 3, 4, 5]
    sample_even = [1, 2, 3, 4]
    sample_single = [42]
    sample_empty = []

    result_odd = get_central_item(sample_odd)
    result_even = get_central_item(sample_even)
    result_single = get_central_item(sample_single)
    result_empty = get_central_item(sample_empty)

    print(result_odd)
    print(result_even)
    print(result_single)
    print(result_empty)