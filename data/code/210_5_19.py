from typing import List, Union

def calculate_range(values: List[Union[int, float]]) -> Union[int, float]:
    if not values:
        raise ValueError("Input list is empty")
    
    min_val = max_val = values[0]
    for value in values[1:]:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    
    return (min_val, max_val)

if __name__ == '__main__':
    sample_data = [3.5, 1.2, 7.8, 0.9]
    range_result = calculate_range(sample_data)
    print(f"Range of the data: {range_result}")