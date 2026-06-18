def get_length(iterable):
    return len(list(iterable))
if __name__ == '__main__':
    data = [1, 2, 3]
    print(get_length(data))
    string_data = "hello"
    print(get_length(string_data))
    range_data = range(5)
    print(get_length(range_data))