from typing import List

def calculate_average(data: List[float]) -> float:
    return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    print(calculate_average(sample_data))