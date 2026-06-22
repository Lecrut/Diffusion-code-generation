def calculate_perimeter(length: float, width: float) -> float:
    return 2 * (length + width)

if __name__ == '__main__':
    sample_values = {
        'length': 10.0,
        'width': 5.0
    }
    perimeter = calculate_perimeter(sample_values['length'], sample_values['width'])
    print(perimeter)