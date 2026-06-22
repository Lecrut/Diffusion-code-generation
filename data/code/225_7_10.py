def validate_values(values):
    if not values:
        raise ValueError("Values tuple cannot be empty")
    for value in values:
        if not isinstance(value, (int, float)):
            raise TypeError("All elements must be numbers")

def get_min_max(values1, values2):
    validate_values(values1)
    validate_values(values2)
    min_val = min(min(values1), min(values2))
    max_val = max(max(values1), max(values2))
    return (min_val, max_val)

if __name__ == '__main__':
    sample_data1 = (5, 9, 3, 7)
    sample_data2 = (8, 1, 6, 4)
    print(f"First set of values: {sample_data1}")
    print(f"Second set of values: {sample_data2}")
    result = get_min_max(sample_data1, sample_data2)
    print(f"Overall minimum and maximum: {result}")