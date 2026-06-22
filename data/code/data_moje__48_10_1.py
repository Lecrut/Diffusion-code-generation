def find_max(data):
    if not data:
        return None
    max_val = data[0]
    for val in data:
        if val > max_val:
            max_val = val
    return max_val

if __name__ == '__main__':
    values = [12, 4, 67, 23, 8, 90, 34, 5, 42]
    result = find_max(values)
    print(result)