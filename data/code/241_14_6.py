def calculate_rectangle_area(length, width):
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        raise ValueError("Invalid numerical input provided.")
    return float(length) * float(width)

if __name__ == '__main__':
    sample_length = 10.5
    sample_width = 4.2
    print(calculate_rectangle_area(sample_length, sample_width))