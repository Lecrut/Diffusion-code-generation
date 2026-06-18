def get_length(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    data = [10, 20, 30]
    print(get_length(data))