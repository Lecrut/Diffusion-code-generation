def calculate_parallelogram_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return base * height

if __name__ == '__main__':
    try:
        base = 10
        height = 5
        area = calculate_parallelogram_area(base, height)
        print(f"Area of parallelogram with base {base} and height {height}: {area}")
    except ValueError as e:
        print(e)