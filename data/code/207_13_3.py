def find_max_stream(data_stream):
    if not data_stream:
        return
    max_val = data_stream[0]
    yield max_val
    for num in data_stream[1:]:
        if num > max_val:
            max_val = num
        yield max_val
if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Stream of data:", sample_data)
    for max_element in find_max_stream(sample_data):
        print("Max element yielded:", max_element)