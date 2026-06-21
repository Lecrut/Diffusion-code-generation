from functools import reduce
import operator

def calculate_average(numbers):
    if not numbers:
        return 0
    total = reduce(operator.add, numbers)
    average = total / len(numbers)
    return average

if __name__ == '__main__':
    sample_numbers = [5, 10, 15, 20, 25]
    avg_sample = calculate_average(sample_numbers)
    print(avg_sample)

    large_numbers = list(range(1, 1000001))
    avg_large = calculate_average(large_numbers)
    print(avg_large)

    empty_list = []
    avg_empty = calculate_average(empty_list)
    print(avg_empty)