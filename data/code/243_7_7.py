def calculate_circumference(radius):
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    return 2 * 3.141592653589793 * radius
if __name__ == '__main__':
    try:
        result1 = calculate_circumference(5)
        print(f"Circumference with radius 5: {result1}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result2 = calculate_circumference(-2)
        print(f"Circumference with radius -2: {result2}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result3 = calculate_circumference(0)
        print(f"Circumference with radius 0: {result3}")
    except ValueError as e:
        print(f"Error: {e}")