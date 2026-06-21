def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for element in data[1:]:
        if element > largest:
            largest = element
    return largest

if __name__ == '__main__':
    sample_values = [7, 3, 5, 9, 2, 8, 4, 6, 1]
    result = find_largest(sample_values)
    print(result)