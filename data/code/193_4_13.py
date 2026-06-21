from typing import List

def calculate_total(values: List[float]) -> float:
    return sum(values)

if __name__ == '__main__':
    sample_values = [1.5, 2.3, 3.7]
    total = calculate_total(sample_values)
    print(total)