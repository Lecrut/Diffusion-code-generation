def get_middle_value(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    length = len(sequence)
    if length % 2 == 1:
        return sequence[length // 2]
    mid_index = length // 2
    return (sequence[mid_index - 1] + sequence[mid_index]) / 2

if __name__ == '__main__':
    test_odd = [10, 20, 30, 40, 50]
    test_even = [10, 20, 30, 40]
    print(get_middle_value(test_odd))
    print(get_middle_value(test_even))