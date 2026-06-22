def calculate_rectangle_area(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        return length * width
    else:
        return None

if __name__ == '__main__':
    sample_values = {
        'length': 10.5,
        'width': 4.2
    }
    area = calculate_rectangle_area(sample_values['length'], sample_values['width'])
    print(f"Area: {area}")