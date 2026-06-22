def get_max_generator(data_stream):
    max_val = None
    for item in data_stream:
        if max_val is None or item > max_val:
            max_val = item
    yield max_val

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = list(get_max_generator(sample_data))
    print(result)