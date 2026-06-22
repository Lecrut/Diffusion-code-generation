def triangle_area(base: float, height: float) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")
    return 0.5 * base * height

if __name__ == '__main__':
    print(triangle_area(10, 5))