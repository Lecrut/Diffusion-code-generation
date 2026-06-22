from typing import List, Union

def find_minimum(values: List[Union[int, float]]) -> Union[int, float]:
    if not values:
        raise ValueError("The list must not be empty")
    
    current_min: Union[int, float] = values[0]
    for i in range(1, len(values)):
        val = values[i]
        if val < current_min:
            current_min = val
    return current_min

if __name__ == '__main__':
    sample_data: List[int] = [34, -5, 12, 0, 99, -10, 45]
    result: Union[int, float] = find_minimum(sample_data)
    print(result)