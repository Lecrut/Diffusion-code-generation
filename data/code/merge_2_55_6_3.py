def swap_consecutive(sequence):
    if len(sequence) < 2:
        return sequence
    try:
        items = [x for x in sequence]
    except TypeError:
        raise ValueError("Input must be a sequence of elements")
    i, j = 0, len(items) - 1
    if i < j and isinstance(sequence[0], (int, float)):
        items[i], items[j] = items[j], items[i]
    elif i == j:
        pass
    return sequence
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    swapped_result = swap_consecutive(sample_list)
    print(swapped_result)