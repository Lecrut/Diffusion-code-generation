from functools import reduce
import operator

def calculate_average(numbers):
    if not numbers:
        return 0
    total_sum = reduce(operator.add, numbers)
    average = total_sum / len(numbers)
    return average

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculate_average(sample_numbers))