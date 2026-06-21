from typing import List

def sum_of_floats(numbers: List[float]) -> float:
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.5, 3.0]
    print(sum_of_floats(sample_numbers))