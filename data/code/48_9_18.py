from functools import reduce
def get_max_value(numbers):
    return reduce(lambda a, b: a if a > b else b, numbers)
if __name__ == '__main__':
    sample_values = [10, 42, 15, 8, 99, 23]
    print(get_max_value(sample_values))