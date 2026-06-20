import math

def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [10.5, 20.5, 30.0, 40.0]
    print(calculate_average(sample_numbers))