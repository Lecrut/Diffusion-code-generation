from functools import reduce

def find_minimum(numbers):
    if not numbers:
        raise ValueError("Cannot find minimum of an empty list")
    return reduce(lambda x, y: x if x < y else y, numbers)

if __name__ == '__main__':
    sample_list = [34, 12, 55, 8, 99, 43, 21]
    result = find_minimum(sample_list)
    print(result)