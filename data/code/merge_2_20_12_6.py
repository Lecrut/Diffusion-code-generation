from typing import List, Union
def remove_negative_values(values: List[Union[int, float]]) -> List[Union[int, float]]:
    return [v for v in values if v >= 0]
if __name__ == '__main__':
    sample_data = [-5, 10, -3.7, 0, -2, 4.5]
    result = remove_negative_values(sample_data)
    print(result)