def find_largest(values):
    if not values:
        return None
    largest = values[0]
    for value in values[1:]:
        if value > largest:
            largest = value
    return largest

if __name__ == '__main__':
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_largest(data))