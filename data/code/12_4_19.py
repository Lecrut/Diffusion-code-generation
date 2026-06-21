def get_middle_value(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    length = len(sequence)
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        mid_index = length // 2
        return (sequence[mid_index - 1] + sequence[mid_index]) / 2

if __name__ == '__main__':
    odd_sequence = [1, 3, 5, 7, 9]
    even_sequence = [2, 4, 6, 8]
    print(get_middle_value(odd_sequence))
    print(get_middle_value(even_sequence))