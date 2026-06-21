def calculate_parallelogram_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return base * height

if __name__ == '__main__':
    base = 5.0
    height = 3.0
    area = calculate_parallelogram_area(base, height)
    print(area)