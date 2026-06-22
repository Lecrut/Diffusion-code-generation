def get_middle_element(sequence):
    if not sequence:
        raise ValueError("Sequence must not be empty")
    length = len(sequence)
    mid = length // 2
    if length % 2 == 0:
        return (sequence[mid - 1] + sequence[mid]) / 2
    return sequence[mid]

if __name__ == '__main__':
    odd_sequence = [10, 20, 30, 40, 50]
    even_sequence = [10, 20, 30, 40]
    print(get_middle_element(odd_sequence))
    print(get_middle_element(even_sequence))