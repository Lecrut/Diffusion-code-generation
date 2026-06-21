from typing import List

def sum_of_floats(numbers: List[float]) -> float:
    total_sum = 0.0
    for number in numbers:
        total_sum += number
    return total_sum

if __name__ == '__main__':
    sample_values = [1.5, 2.3, 4.8]
    result = sum_of_floats(sample_values)
    print(result)