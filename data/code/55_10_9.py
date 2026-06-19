def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    if any(side < 0 for side in [side_a, side_b, side_c]):
        raise ValueError("Side lengths must be non-negative.")
    return side_a + side_b + side_c

if __name__ == '__main__':
    DEFAULT_SIDE_A = 3.0
    DEFAULT_SIDE_B = 4.0
    DEFAULT_SIDE_C = 5.0
    
    try:
        perimeter = calculate_triangle_perimeter(DEFAULT_SIDE_A, DEFAULT_SIDE_B, DEFAULT_SIDE_C)
        print(f"Side A: {DEFAULT_SIDE_A}")
        print(f"Side B: {DEFAULT_SIDE_B}")
        print(f"Side C: {DEFAULT_SIDE_C}")
        print(f"Perimeter: {perimeter}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")