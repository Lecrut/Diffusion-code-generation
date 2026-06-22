def largest_data_point_generator(values):
    max_val = None
    for value in values:
        if max_val is None or value > max_val:
            max_val = value
        yield max_val

if __name__ == '__main__':
    hard_coded_values = [10, 5, 23, 45, 2, 88, 15, 99]
    largest_value = None
    for result in largest_data_point_generator(hard_coded_values):
        largest_value = result
    print(largest_value)