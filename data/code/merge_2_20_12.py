from typing import List, Union
def remove_negatives(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    return [num for num in numbers if num >= 0]
if __name__ == '__main__':
    sample_data = [-5, 10, -3.5, 0, -2, 7.89]
    result = remove_negatives(sample_data)
    print(result)