def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    if any(side < 0 for side in (side_a, side_b, side_c)):
        raise ValueError("Side lengths cannot be negative.")
    return side_a + side_b + side_c

if __name__ == '__main__':
    try:
        side_a = 3.0
        side_b = 4.0
        side_c = 5.0
        perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(f"Side A: {side_a}")
        print(f"Side B: {side_b}")
        print(f"Side C: {side_c}")
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)