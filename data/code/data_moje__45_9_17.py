from typing import List, Union

Number = Union[int, float]

def get_minimum(values: List[Number]) -> Number:
    if not values:
        raise ValueError("List cannot be empty")
    current_min = values[0]
    for value in values[1:]:
        if value < current_min:
            current_min = value
    return current_min

if __name__ == '__main__':
    sample_data = [5.2, -3, 10, 0, -15.5, 7]
    result = get_minimum(sample_data)
    print(result)