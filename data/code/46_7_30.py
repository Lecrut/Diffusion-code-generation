def calculate_perimeter(sides):
    for side in sides:
        if side <= 0:
            raise ValueError("All sides must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    sample_triangle = [5, 12, 13]
    try:
        perimeter_result = calculate_perimeter(sample_triangle)
        print(perimeter_result)
    except ValueError as e:
        print(e)