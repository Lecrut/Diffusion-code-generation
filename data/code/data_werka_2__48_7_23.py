def calculate_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return base * height

if __name__ == '__main__':
    base = 5.5
    height = 3.2
    area = calculate_area(base, height)
    print(area)