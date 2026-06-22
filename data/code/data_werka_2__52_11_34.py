def calculate_rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

if __name__ == '__main__':
    dimensions = {
        'sample1': {'length': 5.0, 'width': 3.0},
        'sample2': {'length': 7.5, 'width': 2.4}
    }
    
    for name, dim in dimensions.items():
        area = calculate_rectangle_area(dim['length'], dim['width'])
        print(f"Area of {name}: {area}")