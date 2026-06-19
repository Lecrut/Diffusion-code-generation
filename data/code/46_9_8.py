def calculate_perimeter(sides):
    if any(side <= 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    sample_triangle = [7, 24, 25]
    try:
        perimeter = calculate_perimeter(sample_triangle)
        print(perimeter)
    except ValueError as e:
        print(e)