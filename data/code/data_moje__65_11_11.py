def feet_to_inches(feet_values):
    if not isinstance(feet_values, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    converted = []
    for ft in feet_values:
        if not isinstance(ft, (int, float)):
            raise TypeError(f"All elements must be numeric, got {type(ft).__name__}")
        if ft < 0:
            raise ValueError("Feet measurements cannot be negative")
        converted.append(ft * 12)
    return converted

if __name__ == '__main__':
    sample_feet = [1.0, 2.5, 10.125, 0.5]
    inches_result = feet_to_inches(sample_feet)
    print(inches_result)