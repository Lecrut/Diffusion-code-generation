def calculate_triangle_perimeter(a, b, c):
    sides = [a, b, c]
    if any(side <= 0 for side in sides):
        raise ValueError("All side lengths must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(9, 12, 15)
        print(perimeter)
    except ValueError as e:
        print(e)