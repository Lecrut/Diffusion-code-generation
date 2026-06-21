def calculate_perimeter(sides):
    if any(side <= 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")
    perimeter = sum(sides)
    return perimeter

if __name__ == '__main__':
    triangle_measurements = [5, 12, 13]
    try:
        result = calculate_perimeter(triangle_measurements)
        print(result)
    except ValueError as e:
        print(e)