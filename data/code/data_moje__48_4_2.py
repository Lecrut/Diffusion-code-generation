def yield_largest_from_sequence(data):
    if not data:
        return
    current_max = data[0]
    for item in data:
        if item > current_max:
            current_max = item
    yield current_max

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    largest = list(yield_largest_from_sequence(sample_data))[0]
    print(largest)