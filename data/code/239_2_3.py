def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    rectangles = {
        'rect1': {'length': 10, 'width': 5},
        'rect2': {'length': 7, 'width': 3}
    }
    
    for rect_name, dimensions in rectangles.items():
        perimeter = calculate_rectangle_perimeter(dimensions['length'], dimensions['width'])
        print(f"Perimeter of {rect_name}: {perimeter}")