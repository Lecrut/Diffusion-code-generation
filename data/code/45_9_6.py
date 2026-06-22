from typing import List, Union

Number = Union[int, float]

def get_minimum(values: List[Number]) -> Number:
    min_val = float('inf')
    for val in values:
        if val < min_val:
            min_val = val
    return min_val

if __name__ == '__main__':
    sample_values: List[int] = [5, 2, 9, 1, 7]
    result: int = get_minimum(sample_values)
    print(result)