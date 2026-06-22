from functools import reduce

def get_max_value(numbers):
    return reduce(lambda a, b: a if a > b else b, numbers)

if __name__ == '__main__':
    sample_data = [15, 42, 8, 99, 3, 67, 23]
    print(get_max_value(sample_data))