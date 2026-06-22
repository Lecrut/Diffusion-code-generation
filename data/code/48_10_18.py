def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for value in data:
        if value > largest:
            largest = value
    return largest

if __name__ == '__main__':
    values = [10, 5, 8, 20, 15, 7, 12, 9]
    result = find_largest(values)
    print(result)