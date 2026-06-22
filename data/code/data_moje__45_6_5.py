from functools import reduce

def find_min(numbers):
    return reduce(lambda a, b: a if a < b else b, numbers)

if __name__ == '__main__':
    sample_data = [34, 12, 5, 89, 2, 56, 1]
    result = find_min(sample_data)
    print(result)