def find_largest(values):
    if not values:
        return None
    largest = values[0]
    for value in values:
        if value > largest:
            largest = value
    return largest

if __name__ == '__main__':
    sample_data = [10, 45, 3, 89, 22, 56, 99, 12, 78, 33]
    result = find_largest(sample_data)
    print(result)