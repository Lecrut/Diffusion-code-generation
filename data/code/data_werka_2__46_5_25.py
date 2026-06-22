def calculate_triangle_perimeter(a, b, c):
    sides = [a, b, c]
    if not all(isinstance(side, (int, float)) and side > 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")
    return sum(sides)

if __name__ == '__main__':
    sample_values = {'side1': 3.5, 'side2': 4.2, 'side3': 5.1}
    perimeter = calculate_triangle_perimeter(**sample_values)
    print(perimeter)