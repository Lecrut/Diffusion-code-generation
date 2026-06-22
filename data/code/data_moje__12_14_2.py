def get_middle_element(sequence):
    if not hasattr(sequence, '__len__'):
        raise TypeError("Input must be a sequence")
    length = len(sequence)
    if length == 0:
        raise ValueError("Sequence cannot be empty")
    if length % 2 == 1:
        return sequence[length // 2]
    mid = length // 2
    return sequence[mid - 1]

if __name__ == '__main__':
    sample_odd = [1, 2, 3, 4, 5]
    sample_even = [10, 20, 30, 40]
    print(get_middle_element(sample_odd))
    print(get_middle_element(sample_even))