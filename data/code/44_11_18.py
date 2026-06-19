def calculate_perimeter(length: float, width: float) -> float:
    return 2 * (length + width)

if __name__ == '__main__':
    length_sample = 8.0
    width_sample = 6.5
    perimeter_result = calculate_perimeter(length_sample, width_sample)
    print(perimeter_result)