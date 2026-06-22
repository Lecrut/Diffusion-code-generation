def yield_largest_from_sequence():
    data = [10, 45, 23, 89, 12, 67, 5, 91, 34, 78]
    current_max = None
    for val in data:
        if current_max is None or val > current_max:
            current_max = val
        yield val
    yield current_max

if __name__ == '__main__':
    result = yield_largest_from_sequence()
    values = []
    for item in result:
        values.append(item)
    largest = values[-1]
    print(largest)