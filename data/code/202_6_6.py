def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for item in data[1:]:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    sample_series = [15, 8, 42, 3, 99, 22]
    result = find_largest(sample_series)
    print(result)