def calculate_perimeter(length, width):
    try:
        length = float(length)
        width = float(width)
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        perimeter = 2 * (length + width)
        return perimeter
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    sample_length = "5"
    sample_width = "10"
    result = calculate_perimeter(sample_length, sample_width)
    print(result)