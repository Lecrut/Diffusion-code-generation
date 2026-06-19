def calculate_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return base * height

if __name__ == '__main__':
    try:
        base = 8
        height = 6
        area = calculate_area(base, height)
        print(area)
    except ValueError as e:
        print(e)