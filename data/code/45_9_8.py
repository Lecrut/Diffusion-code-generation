from typing import List, Union

Number = Union[int, float]

def find_min(values: List[Number]) -> Number:
    if not values:
        raise ValueError("Cannot find minimum of an empty list")
    current_min = values[0]
    for value in values[1:]:
        if value < current_min:
            current_min = value
    return current_min

if __name__ == '__main__':
    sample_data = [34, 5, 12, 89, 1, 56, 3, 7]
    result = find_min(sample_data)
    print(result)