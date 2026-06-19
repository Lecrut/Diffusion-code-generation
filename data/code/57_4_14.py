def calculate_parallelogram_area(base, height):
    if base <= 0:
        raise ValueError("Base must be a positive number.")
    if height <= 0:
        raise ValueError("Height must be a positive number.")
    return base * height

if __name__ == '__main__':
    try:
        base = 10
        height = 5
        area = calculate_parallelogram_area(base, height)
        print(f"Base: {base}, Height: {height}, Area: {area}")
    except ValueError as e:
        print(e)