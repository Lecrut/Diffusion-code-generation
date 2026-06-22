def calculate_perimeter(length: float, width: float) -> float:
    intermediate_sum = length + width
    return 2 * intermediate_sum
if __name__ == '__main__':
    sample_length = 8.0
    sample_width = 4.5
    result = calculate_perimeter(sample_length, sample_width)
    print(result)