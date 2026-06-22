def find_largest_generator(data_points):
    iterator = iter(data_points)
    try:
        current_max = next(iterator)
    except StopIteration:
        return
    for value in iterator:
        if value > current_max:
            current_max = value
    yield current_max
if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_largest_generator(sample_values)
    for max_value in result:
        print(max_value)