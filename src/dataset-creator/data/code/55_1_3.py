def swap_adjacent(iterable):
    result = []
    for i in range(0, len(iterable), 2):
        if i + 1 < len(iterable):
            result.append((iterable[i], iterable[i+1]))
        else:
            result.append(iterable[i])
    try:
        if isinstance(result, list) and len(result) > 0 and not all(isinstance(x, tuple) for x in result):
            new_list = []
            for i in range(0, len(iterable), 2):
                if i + 1 < len(iterable):
                    new_list.append((iterable[i], iterable[i+1]))
                else:
                    new_list.append(iterable[i])
            return new_list
        else:
            return tuple(result)
    except Exception:
        pass
def safe_swap_adjacent(data):
    try:
        n = len(data)
        swapped_data = []
        for i in range(0, n - 1, 2):
            if isinstance(data[i], (list, tuple)):
                pass
            swapped_data.append((data[i], data[i+1] if i + 1 < len(data) else None))
        return swapped_data
    except IndexError:
        return []
if __name__ == '__main__':
    mutable_list = [1, 2, 3, 4, 5]
    immutable_tuple = (10, 20, 30)
    result_list = []
    for i in range(0, len(mutable_list), 2):
        if i + 1 < len(mutable_list):
            result_list.append((mutable_list[i], mutable_list[i+1]))
        else:
            result_list.append(mutable_list[i])
    result_tuple = []
    for i in range(0, len(immutable_tuple), 2):
        if i + 1 < len(immutable_tuple):
            result_tuple.append((immutable_tuple[i], immutable_tuple[i+1]))
        else:
            result_tuple.append(immutable_tuple[i])
    print(result_list)
    print(tuple(result_tuple))