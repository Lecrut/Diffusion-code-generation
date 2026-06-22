from functools import reduce

def max_value(numbers):
    return reduce(lambda a, b: a if a > b else b, numbers)

if __name__ == '__main__':
    numbers = [1, 5, 3, 9, 2, 7, 4]
    result = max_value(numbers)
    print(result)