def find_largest_number(data):
    largest = None
    for item in data:
        if isinstance(item, int):
            if largest is None or item > largest:
                largest = item
    return largest
if __name__ == '__main__':
    mixed_list = [10, "apple", 5, "banana", 20, "cherry"]
    result = find_largest_number(mixed_list)
    print(result)