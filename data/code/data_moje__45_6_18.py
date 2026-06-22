from functools import reduce

def find_minimum(numbers):
    return reduce(lambda x, y: x if x < y else y, numbers)

if __name__ == '__main__':
    sample_list = [5, 2, 9, 1, 7, 6]
    result = find_minimum(sample_list)
    print(result)