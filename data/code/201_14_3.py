from typing import List

def calculate_average(values: List[float]) -> float:
    if not values:
        return 0.0
    total = sum(values)
    count = len(values)
    average = total / count
    return average

if __name__ == '__main__':
    sample_data = [25, 35, 45, 55, 65]
    result = calculate_average(sample_data)
    print(result)