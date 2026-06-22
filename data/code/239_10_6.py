def calculate_rectangle_perimeter(width, height):
    return 2 * (width + height)
if __name__ == '__main__':
    sample_width = 10
    sample_height = 4
    calculated_perimeter = calculate_rectangle_perimeter(sample_width, sample_height)
    print(calculated_perimeter)