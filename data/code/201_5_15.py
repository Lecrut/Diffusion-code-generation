from math import fsum

def calculate_average(numbers: list[float]) -> float:
    return fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [3.5, 2.1, 4.8, 5.9]
    average = calculate_average(sample_numbers)
    print(average)