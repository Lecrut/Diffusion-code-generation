from functools import reduce

def find_max_number(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)

if __name__ == '__main__':
    sample_numbers = [3, 7, 2, 9, 1, 8]
    max_number = find_max_number(sample_numbers)
    print(max_number)