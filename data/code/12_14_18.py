def get_middle_element(sequence):
    if not isinstance(sequence, (list, tuple, str)):
        raise TypeError("Input must be a list, tuple, or string")
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence cannot be empty")
    if length % 2 == 1:
        return sequence[length // 2]
    mid_index_right = length // 2
    mid_index_left = mid_index_right - 1
    return (sequence[mid_index_left], sequence[mid_index_right])

if __name__ == '__main__':
    data_odd = [1, 2, 3, 4, 5]
    data_even = [1, 2, 3, 4]
    data_string = "hello"
    result_odd = get_middle_element(data_odd)
    result_even = get_middle_element(data_even)
    result_string = get_middle_element(data_string)
    print(result_odd)
    print(result_even)
    print(result_string)