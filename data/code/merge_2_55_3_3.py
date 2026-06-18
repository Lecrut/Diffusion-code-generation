import copy
def swap_adjacent(seq):
    if isinstance(seq, tuple) or not hasattr(seq, '__getitem__'):
        return seq
    result = list(seq)
    n = len(result)
    for i in range(0, n - 1, 2):
        result[i], result[i + 1] = result[i + 1], result[i]
    if isinstance(seq, tuple):
        return tuple(result)
    else:
        return copy.deepcopy(result)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = (100, 200, 300, 400)
    swapped_list = swap_adjacent(sample_list)
    swapped_tuple = swap_adjacent(sample_tuple)
    print(f"Original List: {sample_list}")
    print(f"Swapped List: {swapped_list}")
    print(f"Original Tuple: {sample_tuple}")
    print(f"Swapped Tuple: {swapped_tuple}")