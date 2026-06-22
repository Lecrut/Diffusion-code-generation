def calculate_rectangle_area(width: float, height: float) -> float:
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative")
    return width * height

if __name__ == "__main__":
    sample_width = 5.5
    sample_height = 3.2
    result = calculate_rectangle_area(sample_width, sample_height)
    print(result)