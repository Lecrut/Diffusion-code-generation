from typing import List

def calculate_average(data: List[float]) -> float:
    if not data:
        return 0.0
    total = sum(data)
    count = len(data)
    average = total / count
    return average

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55]
    result = calculate_average(sample_data)
    print(result)