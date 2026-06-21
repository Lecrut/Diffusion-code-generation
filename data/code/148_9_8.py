def find_largest(data):
    if not data:
        raise ValueError("The list is empty")
    largest = data[0]
    for item in data:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    data = [3, 1, 4, 1, 5, 9, 2]
    largest = find_largest(data)
    print(largest)