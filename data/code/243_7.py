def calculate_circumference(radius):
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    return 2 * 3.14159 * radius
if __name__ == '__main__':
    try:
        result1 = calculate_circumference(5)
        print(f"Circumference for radius 5: {result1}")
        result2 = calculate_circumference(0)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        calculate_circumference(-2)
    except ValueError as e:
        print(f"Error caught: {e}")