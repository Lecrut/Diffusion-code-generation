def get_middle_value(sequence):
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence cannot be empty")
    if length % 2 == 1:
        return sequence[length // 2]
    return (sequence[length // 2 - 1] + sequence[length // 2]) / 2

if __name__ == '__main__':
    sample_odd = [10, 20, 30, 40, 50]
    sample_even = [5, 15, 25, 35]
    result_odd = get_middle_value(sample_odd)
    result_even = get_middle_value(sample_even)
    print(result_odd)
    print(result_even)