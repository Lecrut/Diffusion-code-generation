import math

def calculate_average(numbers):
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [15, 25, 35, 45]
    print(calculate_average(sample_numbers))