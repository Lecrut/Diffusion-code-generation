from typing import List

def find_min_value(numbers: List[float]) -> float:
    return min(numbers)

if __name__ == '__main__':
    sample_values = [4.5, 2.3, 9.8, 1.2, 7.6]
    print(find_min_value(sample_values))