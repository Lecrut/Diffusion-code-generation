from functools import reduce

def find_minimum(numbers):
    return reduce(lambda a, b: a if a < b else b, numbers)

if __name__ == '__main__':
    sample_list = [42, 7, 19, 3, 28, 56]
    result = find_minimum(sample_list)
    print(result)