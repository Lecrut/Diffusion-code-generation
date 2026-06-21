def calculate_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return base * height

if __name__ == '__main__':
    base = 9.1
    height = 4.3
    area = calculate_area(base, height)
    print(area)