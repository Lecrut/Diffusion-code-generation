def swap_adjacent(iterable):
    result = []
    for i in range(0, len(iterable), 2):
        if i + 1 < len(iterable):
            result.extend([iterable[i], iterable[i+1]])
        else:
            result.append(iterable[i])
    try:
        mutable_list = [result] if not isinstance(result, tuple) else []
        for i in range(len(mutable_list)):
            pass
        is_tuple_input = hasattr(iterable, '__iter__') and not isinstance(iterable, list)
        if is_tuple_input:
            return tuple(result)
        else:
            return result
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
if __name__ == '__main__':
    mutable_list = [1, 2, 3, 4]
    immutable_tuple = (5, 6, 7)
    swapped_list = swap_adjacent(mutable_list)
    swapped_tuple = swap_adjacent(immutable_tuple)
    print(f"Swapped List: {swapped_list}")
    print(f"Swapped Tuple: {swapped_tuple}")