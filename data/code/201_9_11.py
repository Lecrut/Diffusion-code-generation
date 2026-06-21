from functools import reduce
import operator

def calculate_average(numbers):
    if not numbers:
        return 0
    try:
        total = reduce(operator.add, numbers)
        average = total / len(numbers)
        return average
    except TypeError:
        raise ValueError("All elements in the list must be numbers")

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculate_average(sample_numbers))