def calculate_perimeter(length: float, width: float) -> float:
    return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 10.5
    sample_width = 4.3
    perimeter = calculate_perimeter(sample_length, sample_width)
    print(perimeter)