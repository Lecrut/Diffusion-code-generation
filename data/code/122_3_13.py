import math

def calculate_average(numbers):
    if not numbers:
        return 0.0
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [15, 25, 35, 45]
    average = calculate_average(sample_numbers)
    print(average)