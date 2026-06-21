def get_middle_value(sequence):
    if not sequence:
        raise ValueError("Sequence must not be empty")
    size = len(sequence)
    half_size = size // 2
    if size % 2 == 0:
        lower_index = half_size - 1
    else:
        lower_index = half_size
    return sequence[lower_index]

if __name__ == '__main__':
    sample_odd = [10, 20, 30, 40, 50]
    sample_even = [100, 200, 300, 400]
    sample_single = [999]
    sample_two = [1, 2]
    print(get_middle_value(sample_odd))
    print(get_middle_value(sample_even))
    print(get_middle_value(sample_single))
    print(get_middle_value(sample_two))