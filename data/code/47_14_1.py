def calculate_triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height

if __name__ == '__main__':
    result = calculate_triangle_area(10.0, 5.0)
    print(result)