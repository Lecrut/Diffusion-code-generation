import math

def calculate_average(numbers):
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    numbers = [3.141592653589793, 2.718281828459045, 1.4142135623730951]
    print(calculate_average(numbers))