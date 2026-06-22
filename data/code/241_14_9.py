def calculate_rectangle_area(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        return length * width
    else:
        return None
if __name__ == '__main__':
    sample_length = 5
    sample_width = 3
    area = calculate_rectangle_area(sample_length, sample_width)
    print(area)