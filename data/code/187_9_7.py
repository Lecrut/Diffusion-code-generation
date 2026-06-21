from typing import List

def find_max_value(numbers: List[float]) -> float:
    return max(numbers)

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 1.9]
    print(find_max_value(sample_values))