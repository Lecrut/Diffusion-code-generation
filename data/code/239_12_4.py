def calculate_perimeter(length: float, width: float) -> float:
    return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 5.0
    sample_width = 3.0
    perimeter = calculate_perimeter(sample_length, sample_width)
    print(perimeter)