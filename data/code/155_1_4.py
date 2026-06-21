from functools import reduce

def calculate_total(numbers):
    return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(calculate_total(sample_numbers))