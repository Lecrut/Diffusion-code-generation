def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for value in data:
        if value > largest:
            largest = value
    return largest

if __name__ == '__main__':
    values = [34, 15, 88, 2, 99, 56, 12, 77]
    result = find_largest(values)
    print(result)