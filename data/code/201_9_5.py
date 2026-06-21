from functools import reduce
import operator

def calculate_average(data):
    if not data:
        return 0
    total = reduce(operator.add, data)
    average = total / len(data)
    return average

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(calculate_average(sample_data))