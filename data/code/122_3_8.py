import math

def calculate_average(numbers):
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [12, 34, 56, 78]
    average = calculate_average(sample_numbers)
    print(average)