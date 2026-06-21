from functools import reduce
import operator

def validate_data(data):
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements must be numbers")

def calculate_sum(numbers):
    return reduce(operator.add, numbers)

def find_average(data):
    validate_data(data)
    total = calculate_sum(data)
    average = total / len(data)
    return average

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(find_average(sample_list))