def calculate_perimeter(length: float, width: float) -> float:
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    sample_length = 9.0
    sample_width = 4.5
    result = calculate_perimeter(sample_length, sample_width)
    print(result)