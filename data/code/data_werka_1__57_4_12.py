def validate_dimensions(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")

def calculate_parallelogram_area(base, height):
    validate_dimensions(base, height)
    return base * height

if __name__ == '__main__':
    base = 7
    height = 4
    area = calculate_parallelogram_area(base, height)
    print(f"Base: {base}")
    print(f"Height: {height}")
    print(f"Area of parallelogram: {area}")