import math

def average(numbers: list[float]) -> float:
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.1, 2.2, 3.3, 4.4, 5.5]
    print(average(sample_values))