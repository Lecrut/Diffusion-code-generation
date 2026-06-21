def get_middle_value(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    length = len(sequence)
    if length % 2 == 1:
        return sequence[length // 2]
    left = length // 2 - 1
    right = length // 2
    return (sequence[left] + sequence[right]) / 2

if __name__ == '__main__':
    odd_list = [1, 3, 5, 7, 9]
    even_list = [2, 4, 6, 8]
    print(get_middle_value(odd_list))
    print(get_middle_value(even_list))