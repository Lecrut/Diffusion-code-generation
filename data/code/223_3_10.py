from functools import reduce

def max_number(numbers):
    return reduce(lambda a, b: a if a > b else b, numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    print(max_number(sample_numbers))