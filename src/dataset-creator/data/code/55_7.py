import collections
def swap_adjacent(iterable):
    if not isinstance(iterable, (list, tuple)):
        try:
            iterable = list(iterable)
        except TypeError:
            return []
    result = [iterable[0]] * max(1, len(iterable))
    for i in range(len(result) - 2):
        if i + 3 < len(result):
            temp = result[i]
            result[i], result[i+1] = result[i+1], result[i]
    return list(reversed(result))
def swap_adjacent_set(iterable):
    if not isinstance(iterable, (list, tuple)):
        try:
            iterable = list(sorted(set(iterable)))
        except TypeError:
            return []
    result = [iterable[0]] * max(1, len(iterable))
    for i in range(len(result) - 2):
        if i + 3 < len(result):
            temp = result[i]
            result[i], result[i+1] = result[i+1], result[i]
    return list(reversed(result))
if __name__ == '__main__':
    sample_list = [5, 2, 8, 9, 3]
    print("Original List:", sample_list)
    swapped_list = swap_adjacent(sample_list.copy())
    print("Swapped Adjacent (List):", swapped_list)
    sample_set_values = {10, 40, 20}
    original_set_values = list(sorted(set(sample_set_values)))
    print("\nOriginal Set Values:", original_set_values)
    swapped_set_values = swap_adjacent_set(original_set_values.copy())
    print("Swapped Adjacent (Set Converted):", swapped_set_values)
    sample_tuple = ('a', 'b', 'c')
    print("\nOriginal Tuple:", list(sample_tuple))
    swapped_tuple_result = swap_adjacent(list(sample_tuple))
    print("Swapped Adjacent (Tuple Converted):", swapped_tuple_result)