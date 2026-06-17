import copy
def swap_adjacent(seq):
    if isinstance(seq, tuple) or not hasattr(seq, '__setitem__'):
        return _swap_immutable(list(seq))
    result = list(seq)
    n = len(result)
    for i in range(0, n - 1, 2):
        result[i], result[i + 1] = result[i + 1], result[i]
    return tuple(result)
def _swap_immutable(data):
    if not isinstance(data, (list, set)):
        data = [data]
    n = len(data)
    for i in range(0, n - 1, 2):
        data[i], data[i + 1] = data[i + 1], data[i]
    return tuple(data)
if __name__ == '__main__':
    mutable_list = [10, 20, 30, 40]
    immutable_tuple = (5, 6, 7, 8)
    print("Original List:", mutable_list)
    swapped_list = swap_adjacent(mutable_list)
    if isinstance(swapped_list, list):
        print("Swapped List:", swapped_list)
    else:
        print("Type changed to tuple:", swapped_list)
    print("\nOriginal Tuple:", immutable_tuple)
    swapped_tuple = swap_adjacent(immutable_tuple)
    print("Swapped Tuple:", swapped_tuple)