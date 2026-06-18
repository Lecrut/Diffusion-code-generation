from typing import List
def remove_negatives(numbers: List[float]) -> List[float]:
    return [num for num in numbers if num >= 0]
if __name__ == '__main__':
    sample_data = [-5, -2.3, 10, 4, -7.89, 0, 3.14]
    result = remove_negatives(sample_data)
    print(result)