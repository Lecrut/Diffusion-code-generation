def calculate_area(length: float, width: float) -> float:
    return length * width

if __name__ == '__main__':
    sample_length = 5.0
    sample_width = 3.0
    result = calculate_area(sample_length, sample_width)
    print(result)