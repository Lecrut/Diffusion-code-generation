from functools import reduce

def find_max(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)

if __name__ == '__main__':
    sample_numbers = [7, 3, 9, 1, 5]
    print(find_max(sample_numbers))