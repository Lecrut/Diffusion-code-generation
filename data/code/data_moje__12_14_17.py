def get_middle_element(sequence):
    if not hasattr(sequence, '__getitem__'):
        raise TypeError("Input must be a sequence")
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence must not be empty")
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        mid_index = length // 2
        return (sequence[mid_index - 1] + sequence[mid_index]) / 2

if __name__ == '__main__':
    odd_seq = [1, 2, 3, 4, 5]
    even_seq = [1, 2, 3, 4]
    print(get_middle_element(odd_seq))
    print(get_middle_element(even_seq))