from functools import reduce

def min_complex_by_real(numbers):
    return reduce(lambda x, y: x if x.real < y.real else y, numbers)

if __name__ == '__main__':
    sample_numbers = [3+4j, 1-2j, 5+6j, -7+8j]
    print(min_complex_by_real(sample_numbers))