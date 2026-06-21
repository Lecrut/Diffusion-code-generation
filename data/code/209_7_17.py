from typing import List

def calculate_average(numbers: List[float]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_numbers = [7.7, 8.8, 9.9]
    print(calculate_average(sample_numbers))