def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 5
    sample_width = 3
    print(f"Perimeter of rectangle with length {sample_length} and width {sample_width}: {calculate_perimeter(sample_length, sample_width)}")