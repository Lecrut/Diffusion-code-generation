def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    if any(side < 0 for side in [side_a, side_b, side_c]):
        raise ValueError("Side lengths cannot be negative.")
    return side_a + side_b + side_c

if __name__ == '__main__':
    SAMPLE_SIDES = (5.0, 12.0, 13.0)
    try:
        perimeter = calculate_triangle_perimeter(*SAMPLE_SIDES)
        print(f"Side A: {SAMPLE_SIDES[0]}")
        print(f"Side B: {SAMPLE_SIDES[1]}")
        print(f"Side C: {SAMPLE_SIDES[2]}")
        print(f"Perimeter: {perimeter}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")