def triangle_area(base: float, height: float) -> float:
    return base * height / 2

if __name__ == '__main__':
    base_value = 10.0
    height_value = 5.0
    result = triangle_area(base_value, height_value)
    print(result)