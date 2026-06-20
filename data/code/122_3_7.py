import math

NUMBERS = [15.5, 25.0, 35.5, 45.0]

def calculate_average(numbers):
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    average = calculate_average(NUMBERS)
    print(average)