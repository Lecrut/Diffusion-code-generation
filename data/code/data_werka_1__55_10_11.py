def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    if any(side < 0 for side in (side_a, side_b, side_c)):
        raise ValueError("Side lengths cannot be negative.")
    return side_a + side_b + side_c

if __name__ == '__main__':
    try:
        side1 = 3.0
        side2 = 4.0
        side3 = 5.0
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(f"Sides: {side1}, {side2}, {side3}")
        print(f"Perimeter: {perimeter}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")