import functools

def find_max(numbers):
    return functools.reduce(lambda a, b: a if a > b else b, numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    print(find_max(sample_numbers))