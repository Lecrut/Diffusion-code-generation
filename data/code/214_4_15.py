from functools import reduce

def find_minimum(numbers):
    return reduce(lambda x, y: x if x < y else y, numbers)

if __name__ == '__main__':
    sample_data = [10, 45, 23, 78, 6]
    minimum_value = find_minimum(sample_data)
    print(minimum_value)