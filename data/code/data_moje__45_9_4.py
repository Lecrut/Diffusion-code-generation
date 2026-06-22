from typing import List, Union

Number = Union[int, float]

def get_minimum(values: List[Number]) -> Number:
    if not values:
        raise ValueError("List cannot be empty")
    min_val = values[0]
    for num in values[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_data = [5, 2, 9, 1, 7, 3]
    result = get_minimum(sample_data)
    print(result)