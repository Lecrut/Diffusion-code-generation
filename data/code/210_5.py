def find_min_max(data):
    if not data:
        return
    min_val = data[0]
    max_val = data[0]
    for item in data:
        if item < min_val:
            min_val = item
        if item > max_val:
            max_val = item
    yield min_val
    yield max_val
if __name__ == '__main__':
    large_dataset = range(1000000)
    min_and_max_generator = find_min_max(large_dataset)
    results = list(min_and_max_generator)
    print(f"Minimum value: {results[0]}")
    print(f"Maximum value: {results[1]}")