from functools import reduce
import operator

def calculate_average(data):
    try:
        total = reduce(operator.add, data)
        average = total / len(data)
        return average
    except TypeError:
        return None
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = calculate_average(sample_data)
    print(result)