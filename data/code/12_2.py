def get_central_item(sequence):
    if not sequence:
        raise ValueError("Cannot get central item from an empty sequence")
    length = len(sequence)
    mid_index = length // 2
    if length % 2 == 0:
        return (sequence[mid_index - 1], sequence[mid_index])
    return sequence[mid_index]

if __name__ == '__main__':
    samples = [[1, 2, 3, 4, 5], [10, 20, 30, 40], [], 'abc', [42]]
    for s in samples:
        try:
            result = get_central_item(s)
            print(result)
        except ValueError as e:
            print(f"Error: {e}")