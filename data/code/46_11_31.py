def calculate_triangle_perimeter(side1, side2, side3):
    if not all(isinstance(side, (int, float)) and side > 0 for side in [side1, side2, side3]):
        raise ValueError("Side lengths must be positive numbers.")
    
    perimeter = sum([side1, side2, side3])
    return perimeter

if __name__ == '__main__':
    try:
        side_a = 7.0
        side_b = 9.5
        side_c = 6.3
        triangle_perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(f"The perimeter of the triangle is: {triangle_perimeter}")
    except ValueError as e:
        print(e)