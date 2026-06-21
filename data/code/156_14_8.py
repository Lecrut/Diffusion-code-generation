import math

def calculate_average(numbers):
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [1.2, 3.4, 5.6, 7.8]
    average = calculate_average(sample_numbers)
    print(average)