from typing import List

def sum_of_floats(numbers: List[float]) -> float:
    return sum(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5]
    result = sum_of_floats(sample_values)
    print(result)