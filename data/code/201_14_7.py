from typing import List

def calculate_average(values: List[float]) -> float:
    if not values:
        return 0.0
    total_sum = sum(values)
    count = len(values)
    average = total_sum / count
    return average

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55]
    result = calculate_average(sample_data)
    print(result)