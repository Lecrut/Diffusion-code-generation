def get_middle_value(sequence):
    if not sequence:
        return None
    n = len(sequence)
    mid_index = n // 2
    if n % 2 == 1:
        return sequence[mid_index]
    else:
        return (sequence[mid_index - 1] + sequence[mid_index]) / 2

if __name__ == "__main__":
    sample_odd = [1, 3, 5, 7, 9]
    sample_even = [2, 4, 6, 8]
    sample_empty = []
    print(get_middle_value(sample_odd))
    print(get_middle_value(sample_even))
    print(get_middle_value(sample_empty))