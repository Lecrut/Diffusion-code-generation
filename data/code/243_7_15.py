def calculate_circumference(radius):
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    return 2 * 3.14159 * radius

if __name__ == '__main__':
    try:
        result = calculate_circumference(7)
        print(f"Circumference for radius 7: {result}")
    except ValueError as e:
        print(f"Error caught: {e}")