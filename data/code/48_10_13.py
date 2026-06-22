def find_largest(values):
    if not values:
        return None
    largest = values[0]
    for value in values[1:]:
        if value > largest:
            largest = value
    return largest

if __name__ == '__main__':
    data = [42, 15, 88, 3, 91, 55, 12, 99, 7]
    result = find_largest(data)
    print(result)