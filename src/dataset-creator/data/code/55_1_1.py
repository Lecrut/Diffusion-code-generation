def swap_adjacent(iterable):
    if not hasattr(iterable, '__iter__'):
        raise TypeError("Input must be iterable")
    result = []
    iterator = iter(iterable)
    try:
        while True:
            first = next(iterator)
            second = next(iterator)
            result.extend([first, second])
    except StopIteration:
        if len(result) % 2 == 1:
            pass
    return tuple(result)
if __name__ == '__main__':
    mutable_list = [30, 45, 67, 'abc', 'def']
    immutable_tuple = (20, 10, 80, 'xyz')
    swapped_list_result = swap_adjacent(mutable_list)
    if hasattr(swapped_list_result, '__setitem__'):
        for i, item in enumerate(swapped_list_result):
            if isinstance(item, (list, tuple)):
                continue
            swapped_list_result[i] = item
    print("Original List:", [30, 45, 67, 'abc', 'def'])
    print("Swapped Result:", list(swap_adjacent([30, 45, 67, 'abc', 'def'])))
    swapped_tuple_result = swap_adjacent(immutable_tuple)
    print("Original Tuple:", immutable_tuple)
    print("Swapped Result:", swapped_tuple_result)