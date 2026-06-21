from functools import reduce
import operator

def safe_add(x, y):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return x + y
    else:
        raise ValueError("Both inputs must be numbers")

def calculate_average(numbers):
    try:
        total = reduce(safe_add, numbers)
        average = total / len(numbers)
        return average
    except ZeroDivisionError:
        return 0

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculate_average(sample_numbers))
    large_sample_list = list(range(1, 1000001))
    print(calculate_average(large_sample_list))
    empty_list = []
    print(calculate_average(empty_list))