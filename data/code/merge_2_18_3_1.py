def reverse_sequence(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    def _reverse_helper(start, end):
        while start < end:
            sequence[start], sequence[end] = sequence[end], sequence[start]
            start += 1
            end -= 1
    if isinstance(sequence, (list, tuple)):
        length = len(sequence)
        _reverse_helper(0, length - 1)
if __name__ == '__main__':
    sample_data = [3, 6, 9, 2, 'a', None]
    reversed_sample = list(sample_data)
    reverse_sequence(reversed_sample)
    print(reversed_sample)