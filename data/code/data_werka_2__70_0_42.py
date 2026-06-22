def check_first_and_last(data):
    if not hasattr(data, '__getitem__'):
        raise TypeError("Input must support indexing")
    if len(data) == 0:
        raise ValueError("Input sequence cannot be empty")
    return data[0], data[-1]

if __name__ == '__main__':
    sample_data = [10, 20, 30]
    result = check_first_and_last(sample_data)
    print(result)