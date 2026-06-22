def find_largest(values):
    if not values:
        return None
    largest = values[0]
    for value in values[1:]:
        if value > largest:
            largest = value
    return largest

if __name__ == '__main__':
    data = [10, 45, 2, 88, 15, 99, 34, 67, 50]
    result = find_largest(data)
    print(result)