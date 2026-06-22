from typing import List, Optional, Union

Number = Union[int, float]

def get_minimum(values: List[Number]) -> Optional[Number]:
    if not values:
        return None
    current_min = values[0]
    for value in values[1:]:
        if value < current_min:
            current_min = value
    return current_min

if __name__ == '__main__':
    sample_data: List[Number] = [10, 5, 23, 2, 45, 1]
    result: Optional[Number] = get_minimum(sample_data)
    print(result)