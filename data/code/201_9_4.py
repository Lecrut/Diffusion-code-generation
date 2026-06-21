from functools import reduce
import operator

def calculate_average(numbers):
    if not numbers:
        return 0
    total = reduce(operator.add, numbers)
    average = total / len(numbers)
    return average

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(calculate_average(sample_values))