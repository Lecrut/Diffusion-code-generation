from typing import List, Union, Optional

Number = Union[int, float]

def get_minimum(values: List[Number]) -> Optional[Number]:
    if not values:
        return None
    min_val = values[0]
    for val in values[1:]:
        if val < min_val:
            min_val = val
    return min_val

if __name__ == '__main__':
    sample_data = [5, 2, 9, 1, 7, 6]
    result = get_minimum(sample_data)
    print(result)