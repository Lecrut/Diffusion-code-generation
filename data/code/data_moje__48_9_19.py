import functools

def max_value(data):
    return functools.reduce(lambda x, y: x if x > y else y, data)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(max_value(sample_data))