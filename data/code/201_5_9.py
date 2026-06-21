import math

def calculate_average(numbers: list[float]) -> float:
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 5.6]
    average = calculate_average(sample_values)
    print(f"The average is: {average}")