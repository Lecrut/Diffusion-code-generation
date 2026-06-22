from functools import reduce

def find_max_in_list(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    max_number = find_max_in_list(sample_numbers)
    print(max_number)