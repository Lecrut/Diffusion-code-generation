PERIMETER_FACTOR = 2

def calculate_rectangle_perimeter(width, height):
    return PERIMETER_FACTOR * (width + height)

if __name__ == '__main__':
    sample_width = 8
    sample_height = 6
    result = calculate_rectangle_perimeter(sample_width, sample_height)
    print(result)