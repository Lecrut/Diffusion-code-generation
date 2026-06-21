def calculate_perimeter(sides):
    if not all(isinstance(side, (int, float)) and side > 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    triangle_sides = [5, 12, 13]
    try:
        perimeter = calculate_perimeter(triangle_sides)
        print(perimeter)
    except ValueError as e:
        print(e)