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
    large_dataset = [3.14, 1.618, 2.718, 0.577, 9.999, -10.5, 42.0, -5.3]
    results = find_min_max(large_dataset)
    for value in results:
        print(value)