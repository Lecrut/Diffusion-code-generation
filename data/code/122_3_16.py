import math

def calculate_average(numbers):
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    test_values = [15.2, 25.3, 35.4, 45.5]
    average_result = calculate_average(test_values)
    print(average_result)