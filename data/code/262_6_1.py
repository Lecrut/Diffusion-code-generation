def find_min_max(data):
    if not data:
        return
    minimum = data[0]
    maximum = data[0]
    for item in data[1:]:
        if item < minimum:
            minimum = item
        if item > maximum:
            maximum = item
    yield minimum
    yield maximum
if __name__ == '__main__':
    large_list = [3.14, 1.618, 2.718, 0.577, 99.99, -100.5, 42]
    min_max_generator = find_min_max(large_list)
    print("Minimum and Maximum values:")
    for value in min_max_generator:
        print(value)