def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for value in data[1:]:
        if value > largest:
            largest = value
    return largest

if __name__ == '__main__':
    sample_values = [3, 7, 2, 9, 4, 15, 8, 1]
    result = find_largest(sample_values)
    print(result)