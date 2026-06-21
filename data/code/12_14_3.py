def get_middle_element(sequence):
    if not isinstance(sequence, (list, tuple, str)):
        raise TypeError("Input must be a list, tuple, or string")
    if len(sequence) == 0:
        raise ValueError("Input sequence cannot be empty")
    length = len(sequence)
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        mid_right = length // 2
        mid_left = mid_right - 1
        return (sequence[mid_left], sequence[mid_right])

if __name__ == '__main__':
    test_odd = [1, 2, 3, 4, 5]
    test_even = [10, 20, 30, 40]
    test_string = "hello"
    print(get_middle_element(test_odd))
    print(get_middle_element(test_even))
    print(get_middle_element(test_string))