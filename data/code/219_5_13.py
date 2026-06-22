from functools import reduce

def max_integer(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, 2]
    print(max_integer(sample_numbers))