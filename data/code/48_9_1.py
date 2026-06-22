from functools import reduce

def get_max_value(numbers):
    return reduce(lambda a, b: a if a > b else b, numbers)

if __name__ == '__main__':
    sample_array = [3, 7, 2, 9, 4, 1, 8]
    print(get_max_value(sample_array))