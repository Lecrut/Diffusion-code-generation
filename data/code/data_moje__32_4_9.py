def calculate_rectangle_area(width: float, height: float) -> float:
    if not isinstance(width, (int, float)):
        raise TypeError("width must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("height must be a number")
    if width <= 0:
        raise ValueError("width must be positive")
    if height <= 0:
        raise ValueError("height must be positive")
    return width * height

if __name__ == '__main__':
    result = calculate_rectangle_area(5, 10)
    print(result)