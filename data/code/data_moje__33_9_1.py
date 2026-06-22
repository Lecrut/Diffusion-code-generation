import math

def calculate_triangle_area(base, height):
    try:
        base_value = float(base)
        height_value = float(height)
        if base_value <= 0 or height_value <= 0:
            raise ValueError("Base and height must be positive numbers.")
        return 0.5 * base_value * height_value
    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid input: {e}")

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    result = calculate_triangle_area(sample_base, sample_height)
    print(result)
    sample_base_str = 20
    sample_height_str = "7.5"
    result_str = calculate_triangle_area(sample_base_str, sample_height_str)
    print(result_str)
    try:
        calculate_triangle_area(-5, 10)
    except ValueError as error:
        print(error)
    try:
        calculate_triangle_area("abc", 10)
    except ValueError as error:
        print(error)