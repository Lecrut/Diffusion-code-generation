import functools

def sum_of_numbers(numbers):
    return functools.reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(sum_of_numbers(sample_numbers))