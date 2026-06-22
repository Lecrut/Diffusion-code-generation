def find_largest(values):
    if not values:
        raise ValueError("List must not be empty")
    
    largest = values[0]
    for i in range(1, len(values)):
        if values[i] > largest:
            largest = values[i]
    return largest

if __name__ == '__main__':
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_largest(data)
    print(result)