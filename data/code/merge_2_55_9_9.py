def swap_adjacent(values):
    if not isinstance(values, (list, tuple)):
        return "Input must be a list or tuple."
    result = []
    for i in range(0, len(values), 2):
        if i + 1 < len(values):
            result.append(values[i])
            result.append(values[i + 1])
        else:
            result.append(values[i])
    return tuple(result)
if __name__ == '__main__':
    sample_data = [4, 2, 6, 8]
    swapped_result = swap_adjacent(sample_data)
    print(swapped_result)