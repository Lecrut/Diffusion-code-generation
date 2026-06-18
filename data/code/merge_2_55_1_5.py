def swap_adjacent(iterable):
    result = []
    for i in range(0, len(iterable), 2):
        if i + 1 < len(iterable):
            result.append(iterable[i])
            result.append(iterable[i+1])
        else:
            result.append(iterable[i])
    return result
if __name__ == '__main__':
    mutable_list = [4, 2, 6, 8]
    immutable_tuple = (5, 3, 7)
    swapped_list = swap_adjacent(mutable_list)
    print("Original List:", mutable_list)
    swapped_mutable = swap_adjacent(mutable_list.copy()) if isinstance(mutable_list, list) else None
    original_tuple = immutable_tuple
    swapped_immutable = tuple(swap_adjacent(list(original_tuple)))
    def swap_in_place(lst):
        n = len(lst)
        for i in range(0, n - 1, 2):
            lst[i], lst[i+1] = lst[i+1], lst[i]
        return lst
    swap_in_place(mutable_list)
    print("Swapped List:", mutable_list)
    swapped_tuple_result = tuple(swap_adjacent(list(immutable_tuple))) if isinstance(immutable_tuple, tuple) else None
    final_tuple_output = swap_in_place(list(immutable_tuple))
    print("Swapped Tuple:", tuple(final_tuple_output))