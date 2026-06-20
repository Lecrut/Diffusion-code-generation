def calculate_perimeter(length, width):
    try:
        l = float(length)
        w = float(width)
        if l <= 0 or w <= 0:
            return "Error: Dimensions must be positive numbers."
        return 2 * (l + w)
    except ValueError:
        return "Error: Input must be numeric."

if __name__ == '__main__':
    sample_length = "10.5"
    sample_width = "5"
    result = calculate_perimeter(sample_length, sample_width)
    print(result)