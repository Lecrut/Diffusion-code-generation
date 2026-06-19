def calculate_perimeter(length, width):
    try:
        length = float(length)
        width = float(width)
        perimeter = 2 * (length + width)
        return perimeter
    except ValueError:
        return "Invalid input: Please enter numeric values for length and width."

if __name__ == '__main__':
    sample_length = '5'
    sample_width = '3'
    result = calculate_perimeter(sample_length, sample_width)
    print(result)