import functools

def find_max_stream(data_stream):
    if not data_stream:
        return None
    current_max = functools.reduce(lambda x, y: x if x > y else y, data_stream)
    return current_max

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Stream of data:", sample_data)
    max_val = find_max_stream(sample_data)
    print("Maximum value:", max_val)