def calculate_area(width: float, height: float) -> float:
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative numbers.")
    return width * height

if __name__ == '__main__':
    print(calculate_area(5.0, 3.0))