def calculate_range(values: list) -> tuple:
    if not all(isinstance(x, (int, float)) for x in values):
        raise ValueError("All elements in the list must be numbers")
    return min(values), max(values)

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9]
    try:
        range_result = calculate_range(sample_values)
        print(f"Range: {range_result}")
    except ValueError as e:
        print(e)