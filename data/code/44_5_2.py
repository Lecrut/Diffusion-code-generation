def calculate_perimeter(dimensions):
    if len(dimensions) != 2:
        raise ValueError("Input list must contain exactly two dimensions (length and width).")
    length = dimensions[0]
    width = dimensions[1]
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Dimensions must be numeric values.")
    perimeter = 2 * (length + width)
    return perimeter
if __name__ == '__main__':
    sample_dimensions_valid = [10, 5]
    sample_dimensions_invalid_count = [10, 5, 2]
    sample_dimensions_invalid_type = [10, "five"]
    try:
        perimeter1 = calculate_perimeter(sample_dimensions_valid)
        print(f"Perimeter for {sample_dimensions_valid}: {perimeter1}")
    except (ValueError, TypeError) as e:
        print(f"Error processing {sample_dimensions_valid}: {e}")
    try:
        calculate_perimeter(sample_dimensions_invalid_count)
    except (ValueError, TypeError) as e:
        print(f"Error processing {sample_dimensions_invalid_count}: {e}")
    try:
        calculate_perimeter(sample_dimensions_invalid_type)
    except (ValueError, TypeError) as e:
        print(f"Error processing {sample_dimensions_invalid_type}: {e}")