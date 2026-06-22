def calculate_rectangle_area(length, width):
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        raise ValueError("Both length and width must be numbers.")
    return float(length) * float(width)

if __name__ == '__main__':
    sample_length = 10.5
    sample_width = 4.2
    area = calculate_rectangle_area(sample_length, sample_width)
    print(f"Length: {sample_length}")
    print(f"Width: {sample_width}")
    print(f"Area: {area:.2f}")