def validate_side_length(side: float) -> None:
    if side <= 0:
        raise ValueError(f"Side length must be positive, but got {side}")

def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    validate_side_length(side_a)
    validate_side_length(side_b)
    validate_side_length(side_c)
    return side_a + side_b + side_c

if __name__ == '__main__':
    try:
        side_a = 3.0
        side_b = 4.0
        side_c = 5.0
        perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(f"Sides: {side_a}, {side_b}, {side_c}")
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(f"Error: {e}")