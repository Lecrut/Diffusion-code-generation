from typing import Tuple

def sum_three_integers(numbers: Tuple[int, int, int]) -> int:
    return numbers[0] + numbers[1] + numbers[2]

if __name__ == '__main__':
    sample_values = (7, 8, 9)
    result = sum_three_integers(sample_values)
    print(result)