from typing import List, Union
def remove_negative_values(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    return [num for num in numbers if num >= 0]
if __name__ == '__main__':
    sample_data = [-5, -2.3, 10, -7.89, 0, 42]
    result = remove_negative_values(sample_data)
    print(result)