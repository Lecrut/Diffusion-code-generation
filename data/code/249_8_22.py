def find_largest(data):
    if not data:
        return None

    largest = data[0]
    for item in data[1:]:
        if isinstance(largest, str) and isinstance(item, str):
            if item > largest:
                largest = item
        elif isinstance(largest, (int, float)) and isinstance(item, (int, float)):
            if item > largest:
                largest = item
        else:
            raise TypeError("Mixed types in tuple comparison")

    return largest

if __name__ == '__main__':
    list1 = [(5, "apple"), (3, "banana"), (8, "cherry")]
    print(find_largest(list1))