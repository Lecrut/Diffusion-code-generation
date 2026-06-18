def swap_adjacent(values):
    if not isinstance(values, list) and len(values) > 0:
        return [values]
    result = []
    i = 0
    while i < len(values):
        if i + 1 >= len(values):
            result.append(values[i])
        else:
            if len(values) > 0:
                result.append(values[i + 1])
                result.append(values[i])
        i += 2
    return result
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4]
    output = swap_adjacent(sample_data)
    print(output)