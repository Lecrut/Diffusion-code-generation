def calculate_parallelogram_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return base * height

if __name__ == '__main__':
    base = 7
    height = 4
    result = calculate_parallelogram_area(base, height)
    print(result)