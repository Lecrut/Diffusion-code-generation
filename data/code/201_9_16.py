from functools import reduce
import operator

def calculate_average(numbers):
    if not numbers:
        return 0
    total = reduce(operator.add, numbers)
    average = total / len(numbers)
    return average

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(calculate_average(sample_numbers))
    large_sample_numbers = list(range(1, 1000001))
    print(calculate_average(large_sample_numbers))
    empty_list = []
    print(calculate_average(empty_list))