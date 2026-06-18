from typing import List
def sort_numeric_values(numbers: List[float]) -> List[float]:
    return sorted(numbers)
if __name__ == '__main__':
    sample_data = [64, 34, 25, 12, 98]
    result: List[float] = sort_numeric_values(sample_data)
    print(result)