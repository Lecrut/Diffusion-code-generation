def is_valid_triangle_side(side):
    return side > 0

def calculate_perimeter(sides):
    if not all(is_valid_triangle_side(side) for side in sides):
        raise ValueError("All sides must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    triangle_sides = [7, 9, 12]
    perimeter = calculate_perimeter(triangle_sides)
    print(perimeter)