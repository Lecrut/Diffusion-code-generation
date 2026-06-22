def calculate_triangle_perimeter(side1, side2, side3):
    if not (side1 > 0 and side2 > 0 and side3 > 0):
        raise ValueError("Invalid triangle: Side lengths must be positive.")
    
    sides = [side1, side2, side3]
    perimeter = sum(sides)
    return perimeter

if __name__ == '__main__':
    a = 5
    b = 12
    c = 13
    try:
        result = calculate_triangle_perimeter(a, b, c)
        print(f"The perimeter of the triangle with sides {a}, {b}, and {c} is: {result}")
    except ValueError as e:
        print(e)