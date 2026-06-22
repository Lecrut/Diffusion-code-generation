def calculate_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    test_values = [(10, 5), (12, 8), (15, 7)]
    for base, height in test_values:
        area = calculate_area(base, height)
        print(f"The area of a triangle with base {base} and height {height} is: {area}")