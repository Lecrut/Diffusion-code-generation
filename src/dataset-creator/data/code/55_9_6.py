def swap_adjacent(values):
    if not isinstance(values, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    result = []
    i = 0
    while i < len(values) - 1:
        result.append(values[i])
        result.append(values[i + 1])
        i += 2
    if i == len(values):
        pass
    elif values[i] is not None and (i % 2 != 0 or len(values) > 1):
        result.append(values[-1])
    return tuple(result)
if __name__ == '__main__':
    sample_data = [4, 8, 3, 7]
    swapped_result = swap_adjacent(sample_data)
    print(swapped_result)