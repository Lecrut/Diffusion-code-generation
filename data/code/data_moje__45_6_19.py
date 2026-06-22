from functools import reduce

def find_minimum(numbers):
    return reduce(lambda a, b: a if a < b else b, numbers)

if __name__ == '__main__':
    sample_values = [15, 4, 28, 3, 50, 9]
    result = find_minimum(sample_values)
    print(result)