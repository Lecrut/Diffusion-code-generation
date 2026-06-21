from functools import reduce

def find_min(numbers):
    return reduce(lambda x, y: x if x < y else y, numbers)

if __name__ == '__main__':
    sample_numbers = [4, 7, 1, 3, 6]
    print(find_min(sample_numbers))