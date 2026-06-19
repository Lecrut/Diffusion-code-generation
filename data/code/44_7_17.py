def calculate_perimeter(length, width):
    try:
        length = float(length)
        width = float(width)
        if length <= 0 or width <= 0:
            return "Length and width must be positive numbers."
        return 2 * (length + width)
    except ValueError:
        return "Invalid input: Please enter numeric values for length and width."

if __name__ == '__main__':
    sample_length = '7'
    sample_width = '3'
    result = calculate_perimeter(sample_length, sample_width)
    print(result)