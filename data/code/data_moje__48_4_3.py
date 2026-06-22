def largest_data_point_generator(data):
    current_max = None
    for item in data:
        if current_max is None or item > current_max:
            current_max = item
            yield current_max

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = None
    for max_val in largest_data_point_generator(sample_data):
        result = max_val
    print(result)