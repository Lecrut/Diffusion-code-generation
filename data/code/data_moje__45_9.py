from typing import List, Union

Number = Union[int, float]

def get_min_value(values: List[Number]) -> Number:
    if not values:
        raise ValueError("List must not be empty")
    min_val: Number = values[0]
    for val in values[1:]:
        if val < min_val:
            min_val = val
    return min_val

if __name__ == '__main__':
    sample_list: List[Number] = [3, 1, 4, 1, 5, 9, 2, 6]
    result: Number = get_min_value(sample_list)
    print(result)