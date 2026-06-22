def calculate_perimeter(length: int, width: int) -> int:
    return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 5
    sample_width = 3
    print(calculate_perimeter(sample_length, sample_width))