from typing import Tuple

def calculate_signed_difference(pair: Tuple[int, int]) -> int:
    num1, num2 = pair
    return num1 - num2
if __name__ == '__main__':
    sample_values = (30, 15)
    print(calculate_signed_difference(sample_values))