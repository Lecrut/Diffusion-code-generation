def get_central_item(sequence):
    if not sequence:
        return None
    length = len(sequence)
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        return (sequence[length // 2 - 1], sequence[length // 2])

if __name__ == '__main__':
    sample_odd = [1, 2, 3, 4, 5]
    sample_even = [1, 2, 3, 4, 5, 6]
    sample_single = [42]
    sample_empty = []

    print(get_central_item(sample_odd))
    print(get_central_item(sample_even))
    print(get_central_item(sample_single))
    print(get_central_item(sample_empty))