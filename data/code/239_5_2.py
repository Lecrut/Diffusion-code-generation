def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 5
    sample_width = 3
    perimeter = calculate_rectangle_perimeter(sample_length, sample_width)
    print(perimeter)