def swap_adjacent(values):
    if not isinstance(values, (list, tuple)):
        return "Input must be a list or tuple."
    result = []
    for i in range(0, len(values), 2):
        if i + 1 < len(values):
            result.extend([values[i], values[i+1]])
        else:
            result.append(values[i])
    return result
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    swapped_result = swap_adjacent(sample_list)
    print(swapped_result)