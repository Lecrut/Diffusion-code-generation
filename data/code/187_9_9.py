from typing import List

def find_max_value(numbers: List[float]) -> float:
    return max(numbers)

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 1.618, 0.577]
    print(find_max_value(sample_values))