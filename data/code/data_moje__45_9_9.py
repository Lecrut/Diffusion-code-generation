from typing import List
from typing import Union

Numeric = Union[int, float]

def get_min(values: List[Numeric]) -> Numeric:
    if not values:
        raise ValueError("List must not be empty")
    min_val = values[0]
    for val in values[1:]:
        if val < min_val:
            min_val = val
    return min_val

if __name__ == '__main__':
    sample_list = [34, -1, 7, 23, 15]
    result = get_min(sample_list)
    print(result)