def calculate_rectangle_area(length, width):
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        return None
    area = length * width
    return area

if __name__ == '__main__':
    sample_length = 10.5
    sample_width = 4.2
    result = calculate_rectangle_area(sample_length, sample_width)
    if result is not None:
        print(f"Area: {result}")
    else:
        print("Error: Invalid numerical input provided.")