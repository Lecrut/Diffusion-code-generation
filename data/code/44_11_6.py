def calculate_perimeter(length: float, width: float) -> float:
    return 2 * (length + width)

if __name__ == '__main__':
    dimensions = {
        'length': 8.0,
        'width': 3.5
    }
    perimeter = calculate_perimeter(dimensions['length'], dimensions['width'])
    print(perimeter)