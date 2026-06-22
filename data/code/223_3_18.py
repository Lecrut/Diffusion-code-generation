from functools import reduce

def find_maximum(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)

if __name__ == '__main__':
    sample_values = [8, 3, 15, 2]
    max_value = find_maximum(sample_values)
    print(max_value)