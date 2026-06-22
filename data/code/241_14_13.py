def calculate_rectangle_area(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        return length * width
    else:
        return None

if __name__ == '__main__':
    sample_length = 10.5
    sample_width = 4.2
    area = calculate_rectangle_area(sample_length, sample_width)
    print(f"Area of the rectangle with length {sample_length} and width {sample_width} is: {area:.2f}")