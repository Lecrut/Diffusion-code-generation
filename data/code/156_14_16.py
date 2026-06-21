import math

def calculate_average(numbers):
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [1.23, 4.56, 7.89]
    average = calculate_average(sample_numbers)
    print(average)