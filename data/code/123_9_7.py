from functools import reduce

SUM_CONSTANT = 0

def sum_numbers(numbers):
    return reduce(lambda x, y: x + y, numbers, SUM_CONSTANT)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(sum_numbers(sample_values))