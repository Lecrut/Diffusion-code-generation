def calculate_area(width: float, height: float) -> float:
    return width * height

if __name__ == '__main__':
    sample_width = 8.0
    sample_height = 3.5
    area = calculate_area(sample_width, sample_height)
    print(f"The area of the rectangle with width {sample_width} and height {sample_height} is {area:.2f}")