def calculate_range(values: list[float]) -> tuple[float, float]:
    if not values:
        raise ValueError("Input list cannot be empty")
    
    min_val = max_val = values[0]
    for value in values:
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    
    return (min_val, max_val)

if __name__ == '__main__':
    sample_data = [3.5, 1.2, 7.8, 0.9, 4.5]
    range_result = calculate_range(sample_data)
    print(f"Range: {range_result}")