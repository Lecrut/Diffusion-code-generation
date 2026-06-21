def calculate_perimeter(sides):
    if any(side <= 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    triangle_sides = [5, 12, 13]
    perimeter_value = calculate_perimeter(triangle_sides)
    print(perimeter_value)