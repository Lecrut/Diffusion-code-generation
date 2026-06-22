from functools import reduce

def get_max_value(numbers):
    return reduce(lambda a, b: a if a > b else b, numbers)

if __name__ == '__main__':
    sample_data = [3, 5, 1, 9, 2, 8]
    print(get_max_value(sample_data))