from typing import List
def sort_numbers(numbers: List[float]) -> List[float]:
    return sorted(numbers)
if __name__ == '__main__':
    sample_data = [64, 34, 25, 12, 98, -7]
    result: List[float] = sort_numbers(sample_data)
    print(result)