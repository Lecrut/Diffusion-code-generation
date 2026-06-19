def calculate_triangle_perimeter(sides):
    if any(side <= 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")
    perimeter = sum(sides)
    return perimeter

if __name__ == '__main__':
    triangle_sides = [7, 24, 25]
    try:
        result = calculate_triangle_perimeter(triangle_sides)
        print(result)
    except ValueError as e:
        print(e)