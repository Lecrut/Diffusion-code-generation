def calculate_rectangle_perimeter(width, height):
    perimeter = 2 * (width + height)
    return perimeter

if __name__ == '__main__':
    sample_width = 7
    sample_height = 3
    result = calculate_rectangle_perimeter(sample_width, sample_height)
    print(result)