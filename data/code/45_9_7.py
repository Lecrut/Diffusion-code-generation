from typing import List, Union

Number = Union[int, float]

def get_minimum(values: List[Number]) -> Number:
    if not values:
        raise ValueError("Cannot find minimum of an empty list")
    min_val = values[0]
    for val in values[1:]:
        if val < min_val:
            min_val = val
    return min_val

if __name__ == '__main__':
    sample_values: List[Number] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    result = get_minimum(sample_values)
    print(result)