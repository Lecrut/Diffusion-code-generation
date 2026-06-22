def calculate_triangle_area(base: float, height: float) -> float:
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if base < 0:
        raise ValueError("Base cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    return 0.5 * base * height

if __name__ == '__main__':
    result = calculate_triangle_area(10, 5)
    print(result)