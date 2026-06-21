def validate_sides(sides):
    for side in sides:
        if side <= 0:
            raise ValueError("All sides must be positive numbers.")

def calculate_perimeter(sides):
    validate_sides(sides)
    return sum(sides)

if __name__ == '__main__':
    triangle_sides = [5, 12, 13]
    perimeter = calculate_perimeter(triangle_sides)
    print(perimeter)