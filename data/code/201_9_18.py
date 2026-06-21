from functools import reduce
import operator

def safe_add(x, y):
    try:
        return x + y
    except TypeError:
        return None

def calculate_average(numbers):
    if not numbers:
        return 0
    total = reduce(safe_add, numbers)
    count = len([num for num in numbers if isinstance(num, (int, float))])
    return total / count if count > 0 else 0

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 'a', 40, 50]
    print(calculate_average(sample_numbers))