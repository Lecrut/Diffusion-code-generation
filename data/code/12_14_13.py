def get_middle_element(sequence):
    if not isinstance(sequence, (list, tuple, str)):
        raise TypeError("Input must be a list, tuple, or string.")
    if len(sequence) == 0:
        raise ValueError("Sequence must not be empty.")
    length = len(sequence)
    mid_index = (length - 1) // 2
    return sequence[mid_index]

if __name__ == '__main__':
    odd_sequence = [10, 20, 30, 40, 50]
    even_sequence = [10, 20, 30, 40]
    string_sequence = "abcdef"
    print(get_middle_element(odd_sequence))
    print(get_middle_element(even_sequence))
    print(get_middle_element(string_sequence))