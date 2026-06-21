from functools import reduce

def min_value(numbers):
    return reduce(lambda x, y: x if x < y else y, numbers)

if __name__ == '__main__':
    sample_values = [5, 3, 9, 1, 10]
    print(min_value(sample_values))