import functools
import operator

def calculate_mean(numbers):
    total = functools.reduce(operator.add, numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    values = [1.5, 2.5, 3.5, 4.5, 5.5]
    mean_value = calculate_mean(values)
    print(mean_value)