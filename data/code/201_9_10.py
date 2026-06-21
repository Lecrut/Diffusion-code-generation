from functools import reduce
import operator

def calculate_average(numbers):
    if not numbers:
        return 0
    total = reduce(operator.add, numbers)
    average = total / len(numbers)
    return average

if __name__ == '__main__':
    sample_numbers = [15, 25, 35, 45, 55]
    print(calculate_average(sample_numbers))