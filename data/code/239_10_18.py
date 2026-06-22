def calculate_rectangle_perimeter(width, height):
    return 2 * (width + height)

if __name__ == '__main__':
    sample_width = 10
    sample_height = 5
    result = calculate_rectangle_perimeter(sample_width, sample_height)
    print(result)