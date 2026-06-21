import operator
from functools import reduce

def calculate_average(numbers):
    try:
        total = reduce(operator.add, numbers)
        average = total / len(numbers)
        return average
    except ZeroDivisionError:
        return 0.0
    except TypeError:
        return None

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculate_average(sample_numbers))