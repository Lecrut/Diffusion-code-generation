def swap_adjacent(values):
    if not isinstance(values, list) and not all(isinstance(x, (int, float)) for x in values):
        raise TypeError("Input must be a list of numbers.")
    n = len(values)
    if n == 0:
        return []
    result = [x for i, x in enumerate(values)]
    for i in range(1, n, 2):
        try:
            temp = result[i]
            result[i], result[i-1] = result[i-1], temp
        except IndexError:
            raise ValueError("Invalid index during swap operation.")
    return result
if __name__ == '__main__':
    sample_data = [5, 3, 8, 2, 9, 4]
    print(swap_adjacent(sample_data))