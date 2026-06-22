def find_middle(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise ValueError("Input must be a sequence")
    if len(sequence) == 0:
        raise ValueError("Input sequence must not be empty")
    length = len(sequence)
    mid = length // 2
    if length % 2 == 1:
        return sequence[mid]
    left = sequence[mid - 1:mid]
    right = sequence[mid:mid + 1]
    return (left[0] + right[0]) / 2

if __name__ == '__main__':
    sample_odd = [10, 20, 30, 40, 50]
    sample_even = [10, 20, 30, 40]
    print(find_middle(sample_odd))
    print(find_middle(sample_even))