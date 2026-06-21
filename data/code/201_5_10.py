import math

def average(numbers: list[float]) -> float:
    return math.fsum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 6.7]
    print(average(sample_values))