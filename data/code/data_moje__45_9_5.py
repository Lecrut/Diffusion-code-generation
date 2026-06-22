from typing import List, Optional, Union

Number = Union[int, float]

def get_minimum(values: List[Number]) -> Optional[Number]:
    if not values:
        return None
    minimum = values[0]
    for value in values[1:]:
        if value < minimum:
            minimum = value
    return minimum

if __name__ == '__main__':
    sample_values = [5, 2, 9, 1, 7, 3]
    result = get_minimum(sample_values)
    print(result)