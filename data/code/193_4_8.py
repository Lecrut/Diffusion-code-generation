from typing import List

def sum_of_floats(numbers: List[float]) -> float:
    return sum(numbers)
if __name__ == '__main__':
    sample_numbers = [3.5, 4.2, 0.8, 1.1]
    result = sum_of_floats(sample_numbers)
    print(result)