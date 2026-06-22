def calculate_area(width: float, height: float) -> float:
    if not isinstance(width, (int, float)):
        raise TypeError(f"width must be a number, got {type(width).__name__}")
    if not isinstance(height, (int, float)):
        raise TypeError(f"height must be a number, got {type(height).__name__}")
    if width < 0:
        raise ValueError(f"width must be non-negative, got {width}")
    if height < 0:
        raise ValueError(f"height must be non-negative, got {height}")
    return float(width * height)

if __name__ == '__main__':
    result = calculate_area(10, 20)
    print(result)