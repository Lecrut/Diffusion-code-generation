from functools import reduce

def min_value(numbers):
    return reduce(lambda x, y: x if x < y else y, numbers)

if __name__ == '__main__':
    sample_values = [4, 7, 1, 3, 9]
    print(min_value(sample_values))