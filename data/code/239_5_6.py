PERIMETER_CONSTANT = 2

def calculate_perimeter(length, width):
    return PERIMETER_CONSTANT * (length + width)

if __name__ == '__main__':
    sample_length = 5
    sample_width = 3
    perimeter = calculate_perimeter(sample_length, sample_width)
    print(perimeter)