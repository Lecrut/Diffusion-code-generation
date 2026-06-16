def get_length(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    data = [10, 20, 30]
    print(get_length(data))
    data_str = "hello"
    print(get_length(data_str))
    data_gen = (x * x for x in range(5))
    print(get_length(data_gen))