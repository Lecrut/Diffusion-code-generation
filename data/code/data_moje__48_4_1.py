def yield_largest(data_sequence):
    current_max = None
    for item in data_sequence:
        if current_max is None or item > current_max:
            current_max = item
    yield current_max

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result_generator = yield_largest(sample_data)
    for value in result_generator:
        print(value)