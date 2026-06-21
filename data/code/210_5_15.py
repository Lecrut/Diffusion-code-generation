from typing import List, Iterator

def calculate_range(values: List[float]) -> Iterator[float]:
    if not values:
        raise ValueError("Input list cannot be empty")
    
    min_val = max_val = values[0]
    for value in values:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    
    yield min_val
    yield max_val

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 1.618, 0.577, 0.314]
    range_generator = calculate_range(sample_values)
    print(f"Minimum value: {next(range_generator)}")
    print(f"Maximum value: {next(range_generator)}")