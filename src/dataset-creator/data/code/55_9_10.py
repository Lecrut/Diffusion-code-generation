def swap_adjacent(values):
    if not isinstance(values, (list, tuple)):
        return "Input must be a list or tuple"
    result = []
    i = 0
    while i < len(values) - 1:
        result.append(values[i])
        result.append(values[i + 1])
        i += 2
    if len(values) > 1 and (len(values) % 2 == 1):
        result.append(values[-1])
    return list(result)
if __name__ == '__main__':
    sample_data = [4, 8, 15, 30]
    swapped_result = swap_adjacent(sample_data)
    print(swapped_result)