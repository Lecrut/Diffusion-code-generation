from typing import List

def calculate_total_sum(numbers: List[int]) -> int:
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(calculate_total_sum(sample_numbers))