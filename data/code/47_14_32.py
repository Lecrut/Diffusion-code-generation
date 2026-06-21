def calculate_area(base, height):
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        base1 = 9
        height1 = 4
        area1 = calculate_area(base1, height1)
        print(f"Area of triangle with base {base1} and height {height1}: {area1}")

        base2 = 15
        height2 = 7
        area2 = calculate_area(base2, height2)
        print(f"Area of triangle with base {base2} and height {height2}: {area2}")
    except (TypeError, ValueError) as e:
        print(e)