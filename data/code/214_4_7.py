from functools import reduce

def min_value(numbers):
    return reduce(lambda a, b: a if a < b else b, numbers)

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 10]
    print(min_value(sample_values))