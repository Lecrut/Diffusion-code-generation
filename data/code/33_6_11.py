def triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height

if __name__ == '__main__':
    base_value: float = 10.0
    height_value: float = 5.0
    area: float = triangle_area(base_value, height_value)
    print(area)