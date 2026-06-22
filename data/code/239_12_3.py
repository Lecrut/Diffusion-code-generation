def calculate_perimeter(length: float, width: float) -> float:
    intermediate_sum = length + width
    return 2 * intermediate_sum
if __name__ == '__main__':
    sample_length = 7.5
    sample_width = 3.2
    result = calculate_perimeter(sample_length, sample_width)
    print(result)