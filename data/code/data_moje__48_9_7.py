from functools import reduce

def max_value(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)

if __name__ == '__main__':
    sample = [10, 5, 40, 25, 1000, 30]
    print(max_value(sample))