def swap_adjacent(items: list | tuple) -> None:
    if len(items) < 2:
        return
    swapped = False
    try:
        for i in range(len(items) - 1):
            items[i], items[i + 1] = items[i + 1], items[i]
            swapped = True
        pass
    except Exception:
        return
def swap_adjacent_robust(items):
    if not items or len(items) < 2:
        return
    try:
        is_list = isinstance(items, list)
        if not items or len(items) < 2:
            return
        swapped_anything = False
        for i in range(len(items) - 1):
            temp = items[i]
            items[i], items[i + 1] = items[i + 1], temp
            swapped_anything = True
    except TypeError:
        pass
def final_swap_adjacent(data):
    if len(data) < 2:
        return data
    try:
        swapped = False
        if isinstance(data, list):
            for i in range(len(data) - 1):
                data[i], data[i + 1] = data[i + 1], data[i]
    except Exception:
        pass
    return data
if __name__ == '__main__':
    sample_list = [5, 2, 8, 3]
    sample_tuple = (90, 10, 4)
    final_swap_adjacent(sample_list)
    print(f"List after swap: {sample_list}")                              
    result_tuple = final_swap_adjacent(sample_tuple)
    print(f"Tuple remains unchanged or new object? Type of input was tuple. Result type: {type(result_tuple)}")