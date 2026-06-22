def calculate_perimeter(sides):
    for side in sides:
        if side <= 0:
            raise ValueError("All sides must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    triangle_sides = [3, 4, 5]
    perimeter = calculate_perimeter(triangle_sides)
    print(perimeter)