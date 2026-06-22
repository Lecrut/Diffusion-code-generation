def calculate_area(width: float, height: float) -> float:
    if not isinstance(width, (int, float)):
        raise TypeError("width must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("height must be a number")
    if isinstance(width, bool) or isinstance(height, bool):
        raise TypeError("width and height cannot be booleans")
    if width < 0:
        raise ValueError("width must be non-negative")
    if height < 0:
        raise ValueError("height must be non-negative")
    return width * height

if __name__ == '__main__':
    print(calculate_area(5, 10))