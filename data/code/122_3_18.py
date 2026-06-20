import math

def calculate_average(numbers):
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(calculate_average(sample_numbers))