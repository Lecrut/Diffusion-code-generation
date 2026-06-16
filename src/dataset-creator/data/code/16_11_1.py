def get_length(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    print(get_length(data))
    string_data = "hello"
    print(get_length(string_data))
    range_data = range(0, 10)
    print(get_length(range_data))