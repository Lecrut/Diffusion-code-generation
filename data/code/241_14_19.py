def calculate_rectangle_area(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        area = length * width
        return area
    else:
        return None

if __name__ == '__main__':
    sample_length = 15.75
    sample_width = 3.2
    result = calculate_rectangle_area(sample_length, sample_width)
    if result is not None:
        print(f"Length: {sample_length}, Width: {sample_width}, Area: {result}")
    else:
        print("Invalid input provided.")