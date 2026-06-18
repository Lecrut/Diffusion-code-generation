from typing import List
def sort_numeric_values(values: List[float]) -> List[float]:
    return sorted(values)
if __name__ == '__main__':
    sample_data = [5, 234, -10, 9876, 0.5, 3]
    result: List[float] = sort_numeric_values(sample_data)
    print(result)