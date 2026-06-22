import functools

def find_max(numbers):
    return functools.reduce(lambda a, b: max(a, b), numbers)

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_max(sample_numbers))