def find_largest(data):
    if not data:
        raise ValueError("List is empty")
    largest = data[0]
    for item in data[1:]:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    data = [3, 1, 4, 1, 5, 9, 2]
    try:
        print(find_largest(data))
    except ValueError as e:
        print(e)