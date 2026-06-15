def find_max_stream(data_stream):
    if not data_stream:
        return
    current_max = data_stream[0]
    yield current_max
    for number in data_stream[1:]:
        if number > current_max:
            current_max = number
        yield current_max
if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Stream of data:", sample_data)
    for max_val in find_max_stream(sample_data):
        print(max_val)