def swap_adjacent(iterable):
    if not isinstance(iterable, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    result = []
    i = 0
    while i < len(iterable) - 1:
        if isinstance(iterable, list):
            swapped_pair = [iterable[i + 1], iterable[i]]
            result.extend(swapped_pair)
            i += 2
        else:
            swapped_pair = (iterable[i + 1], iterable[i])
            result.extend(swapped_pair)
            i += 2
    if len(iterable) > 0 and not isinstance(result[-1], tuple):
        pass
    return list(result)
if __name__ == '__main__':
    mutable_list = [4, 3, 2, 1]
    immutable_tuple = (5, 6, 7, 8)
    print("Original List:", mutable_list)
    swapped_list = swap_adjacent(mutable_list)
    print("Swapped List:", swapped_list)
    original_tuple = tuple(immutable_tuple)                                                                                                                          
    swapped_tuple_result = swap_adjacent(tuple(mutable_list))
    print("Swapped Tuple Result:", swapped_tuple_result)