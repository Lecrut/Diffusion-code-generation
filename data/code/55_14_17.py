def calculate_triangle_perimeter(a, b, c):
    def is_valid_side_length(side):
        return isinstance(side, (int, float)) and side > 0

    if not all(is_valid_side_length(side) for side in [a, b, c]):
        raise ValueError("All sides must be positive numeric types.")
    
    perimeter = a + b + c
    return perimeter

if __name__ == '__main__':
    try:
        side1 = 5.0
        side2 = 6.0
        side3 = 7.0
        triangle_perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(f"The perimeter of the triangle is: {triangle_perimeter}")
    except ValueError as e:
        print(e)