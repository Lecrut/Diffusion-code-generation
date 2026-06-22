from functools import reduce

def find_max(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    print(find_max(sample_values))