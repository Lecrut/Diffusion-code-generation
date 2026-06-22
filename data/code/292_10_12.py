def calculate_rectangle_perimeter(length: int, width: int) -> int:
    return 2 * (length + width)

if __name__ == '__main__':
    dimensions = { 'length': 5, 'width': 3 }
    print(calculate_rectangle_perimeter(dimensions['length'], dimensions['width']))