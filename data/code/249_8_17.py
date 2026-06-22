def find_largest(data):
    if not data:
        return None
    type_map = {str: max, int: lambda x, y: x if x > y else y}
    largest = next(iter(data))
    for item in data[1:]:
        if isinstance(largest, str) and isinstance(item, str):
            if largest < item:
                largest = item
        elif isinstance(largest, int) and isinstance(item, int):
            largest = type_map[int](largest, item)
        else:
            return None
    return largest
if __name__ == '__main__':
    list1 = [10, 'apple', 5, 'banana', 20]
    print(find_largest(list1))