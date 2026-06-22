from typing import List, Union

def get_minimum(values: List[Union[int, float]]) -> Union[int, float]:
    if not values:
        raise ValueError("List must not be empty")
    min_val = values[0]
    for val in values[1:]:
        if val < min_val:
            min_val = val
    return min_val

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.1, 5.9]
    result = get_minimum(sample_values)
    print(result)