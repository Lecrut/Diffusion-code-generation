from functools import reduce

def find_minimum(numbers):
    return reduce(lambda a, b: a if a < b else b, numbers)

if __name__ == '__main__':
    sample_list = [5, 2, 9, 1, 7, 3]
    result = find_minimum(sample_list)
    print(result)