from typing import List

def sum_of_floats(numbers: List[float]) -> float:
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be of type int or float.")
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.3, 3.7]
    result = sum_of_floats(sample_numbers)
    print(result)