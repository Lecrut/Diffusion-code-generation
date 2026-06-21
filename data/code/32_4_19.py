def calculate_area(width: float, height: float) -> float:
    if not isinstance(width, (int, float)):
        raise TypeError("Width must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if width < 0:
        raise ValueError("Width cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    return width * height

if __name__ == '__main__':
    result = calculate_area(10, 5)
    print(result)