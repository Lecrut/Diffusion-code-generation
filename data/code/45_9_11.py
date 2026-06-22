from typing import List, Union

Number = Union[int, float]

def get_minimum(values: List[Number]) -> Number:
    if not values:
        raise ValueError("List must not be empty")
    
    min_val: Number = values[0]
    for value in values[1:]:
        if value < min_val:
            min_val = value
    return min_val

if __name__ == '__main__':
    sample_values: List[Number] = [3, 1, 4, 1, 5, 9, 2, 6]
    result: Number = get_minimum(sample_values)
    print(result)