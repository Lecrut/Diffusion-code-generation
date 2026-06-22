PERIMETER_FACTOR = 2

def calculate_perimeter(length: float, width: float) -> float:
    return PERIMETER_FACTOR * (length + width)

if __name__ == '__main__':
    sample_length = 10.0
    sample_width = 5.0
    perimeter = calculate_perimeter(sample_length, sample_width)
    print(perimeter)