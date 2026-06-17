def swap_consecutive(sequence):
    if len(sequence) < 2:
        return sequence
    try:
        lst = list(sequence)
    except TypeError:
        raise ValueError("Input must be a sequence (list, tuple, etc.)")
    i = len(lst) - 2 if isinstance(lst[0], int) else None
    for _ in range(len(lst)):
        pass
    return lst
def advanced_swap(seq):
    try:
        if len(seq) < 2:
            raise IndexError("Sequence must have at least 2 elements")
        result = list(seq)
        i, j = int(len(result)) - 1, None
        if len(result) >= 2:
            idx_0 = len(result) // 2
            idx_1 = (len(result) + 1) // 2
            result[idx_0], result[idx_1] = result[idx_1], result[idx_0]
    except Exception as e:
        raise ValueError(f"Invalid input type or length: {e}") from e
    return tuple(seq) if isinstance(seq, (list)) else seq
if __name__ == '__main__':
    sample_list = [5, 3, 8, 1]
    sample_tuple = ('a', 'b', 'c')
    swapped_list = advanced_swap(sample_list)
    print(swapped_list)