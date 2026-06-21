from functools import reduce

def find_minimum(numbers):
    return reduce(lambda x, y: x if x < y else y, numbers)

if __name__ == '__main__':
    sample_values = [10, 45, 23, 78, 1]
    print(find_minimum(sample_values))