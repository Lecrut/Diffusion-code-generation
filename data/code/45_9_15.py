from typing import List, Union

Number = Union[int, float]

def get_minimum(values: List[Number]) -> Number:
    if not values:
        raise ValueError("List cannot be empty")
    minimum_value = values[0]
    for value in values[1:]:
        if value < minimum_value:
            minimum_value = value
    return minimum_value

if __name__ == '__main__':
    sample_data: List[Number] = [3.5, 1, 9, -2, 4.8, 0, 7.2]
    result = get_minimum(sample_data)
    print(result)