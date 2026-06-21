import operator
from functools import reduce

def calculate_average(data):
    try:
        total = reduce(operator.add, data)
        average = total / len(data)
        return average
    except TypeError:
        return "Error: Non-numeric input types found"
    except ZeroDivisionError:
        return "Error: Empty list"

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(calculate_average(sample_data))