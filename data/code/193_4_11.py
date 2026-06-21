from typing import List

SUM_CONST = 0.0

def sum_of_floats(numbers: List[float]) -> float:
    return sum(numbers) + SUM_CONST

if __name__ == '__main__':
    sample_values = [1.5, 2.3, 3.7]
    result = sum_of_floats(sample_values)
    print(result)