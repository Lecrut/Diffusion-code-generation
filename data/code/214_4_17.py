from functools import reduce

def min_value(numbers):
    return reduce(lambda a, b: a if a < b else b, numbers)

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 7, 5]
    print(min_value(sample_numbers))