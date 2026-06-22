def find_largest_data_point():
    data_points = [10, 25, 5, 89, 3, 42, 17, 60, 99, 14, 73, 31, 88, 4, 56]
    largest = None
    for value in data_points:
        if largest is None or value > largest:
            largest = value
        yield largest

if __name__ == '__main__':
    generator = find_largest_data_point()
    result = None
    for item in generator:
        result = item
    print(result)