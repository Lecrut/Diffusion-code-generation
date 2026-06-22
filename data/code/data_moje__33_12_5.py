def triangle_area(base: float, height: float) -> float:
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base * height

if __name__ == '__main__':
    print(triangle_area(5.0, 3.0))
    print(triangle_area(10.0, 4.0))
    print(triangle_area(7.5, 2.5))