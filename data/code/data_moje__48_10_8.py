def find_max_linear(data):
    if not data:
        raise ValueError("Data list must not be empty")
    max_val = data[0]
    for val in data:
        if val > max_val:
            max_val = val
    return max_val

if __name__ == '__main__':
    values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_max_linear(values)
    print(result)