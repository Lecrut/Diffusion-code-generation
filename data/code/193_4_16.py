from typing import List

def sum_of_floats(numbers: List[float]) -> float:
    total = 0.0
    for number in numbers:
        total += number
    return total
if __name__ == '__main__':
    sample_values = [3.2, 4.5, 6.7]
    result = sum_of_floats(sample_values)
    print(result)