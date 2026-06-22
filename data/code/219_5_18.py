from functools import reduce

MAX_INT = float('-inf')

def find_max_in_list(numbers):
    return reduce(lambda x, y: max(x, y), numbers, MAX_INT)

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_max_in_list(sample_numbers))