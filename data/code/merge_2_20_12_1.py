from typing import List, Union
def remove_negatives(values: List[Union[int, float]]) -> List[Union[int, float]]:
    return [val for val in values if val >= 0]
if __name__ == '__main__':
    sample_data = [-5, -2.3, 10, -4, 0, 7.89, -1]
    result = remove_negatives(sample_data)
    print(result)