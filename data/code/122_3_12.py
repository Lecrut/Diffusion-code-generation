import math

def calculate_average(numbers):
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    test_values = [15, 25, 35]
    average = calculate_average(test_values)
    print(average)