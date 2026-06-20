import math

def calculate_average(numbers):
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    SAMPLE_NUMBERS = [10, 20, 30, 40]
    print(calculate_average(SAMPLE_NUMBERS))