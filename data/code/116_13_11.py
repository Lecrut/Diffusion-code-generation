from typing import Tuple

def sum_three_integers(numbers: Tuple[int, int, int]) -> int:
    first_number, second_number, third_number = numbers
    total_sum = first_number + second_number + third_number
    return total_sum
if __name__ == '__main__':
    sample_values = (10, 20, 30)
    result = sum_three_integers(sample_values)
    print(result)