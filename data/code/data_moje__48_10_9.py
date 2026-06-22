def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for value in data[1:]:
        if value > largest:
            largest = value
    return largest

if __name__ == '__main__':
    sample_values = [34, 19, 42, 8, 91, 55, 2, 88, 76, 3, 50]
    result = find_largest(sample_values)
    print(result)