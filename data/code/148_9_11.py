def find_largest(data):
    if not data:
        raise ValueError("List is empty")
    largest = data[0]
    for item in data:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    sample_data = [7, 3, 5, 9, 2, 12, 8]
    try:
        result = find_largest(sample_data)
        print(result)
    except ValueError as e:
        print(e)