def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    rectangles = [
        {'length': 10, 'width': 5},
        {'length': 7, 'width': 3}
    ]
    for i, dimensions in enumerate(rectangles, start=1):
        perimeter = calculate_rectangle_perimeter(dimensions['length'], dimensions['width'])
        print(f"Perimeter of rectangle {i}: {perimeter}")