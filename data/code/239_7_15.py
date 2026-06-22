def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    dimensions = {
        'length': 10,
        'width': 5
    }
    result = calculate_perimeter(dimensions['length'], dimensions['width'])
    print(f"Perimeter for length {dimensions['length']} and width {dimensions['width']}: {result}")