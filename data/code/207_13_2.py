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
    sample_data_2 = [10, 5, 20, 3, 15]
    print("\nStream of data:", sample_data_2)
    for max_val in find_max_stream(sample_data_2):
        print(max_val)
    sample_data_3 = [7, 7, 7, 7]
    print("\nStream of data:", sample_data_3)
    for max_val in find_max_stream(sample_data_3):
        print(max_val)
    sample_data_4 = []
    print("\nStream of data:", sample_data_4)
    for max_val in find_max_stream(sample_data_4):
        print(max_val)