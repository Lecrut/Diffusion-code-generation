import math

def calculate_average(numbers):
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(calculate_average(sample_numbers))