def calculate_parallelogram_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return base * height

if __name__ == '__main__':
    b = 7.5
    h = 4.0
    print(calculate_parallelogram_area(b, h))