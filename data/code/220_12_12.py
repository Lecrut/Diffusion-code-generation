from typing import Tuple

def calculate_average(numbers: Tuple[int]) -> float:
    if not numbers:
        return 0.0
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    return average

if __name__ == '__main__':
    sample_data = (10, 20, 30, 40, 50)
    avg_result = calculate_average(sample_data)
    print(avg_result)