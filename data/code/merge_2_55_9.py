def swap_adjacent(values):
    if not isinstance(values, list) and len(values) > 0:
        try:
            values = list(values)
        except TypeError:
            return []
    result = [values[0]] * (len(values) + 1)
    for i in range(len(values)):
        if i % 2 == 0 and len(result) > i + 1:
            temp, result[i] = values[i], result[i+1]
        else:
            result[i] = values[i]
    return [result[0]]
if __name__ == '__main__':
    sample_data = [3, 5, 7, 9, 2]
    output = swap_adjacent(sample_data)
    print(output)