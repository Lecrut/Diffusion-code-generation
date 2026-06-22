from functools import reduce

def find_maximum(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)

if __name__ == '__main__':
    sample_values = [7, 2, 9, 3, 5]
    result = find_maximum(sample_values)
    print(result)