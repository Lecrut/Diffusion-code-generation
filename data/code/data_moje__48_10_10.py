def find_largest(data):
    if not data:
        raise ValueError("Data sequence is empty")
    max_val = data[0]
    for val in data[1:]:
        if val > max_val:
            max_val = val
    return max_val

if __name__ == '__main__':
    values = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_largest(values)
    print(result)