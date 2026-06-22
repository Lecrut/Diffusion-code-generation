import math

SHAPE_FORMULAS = {
    'rectangle': lambda length, width: length * width,
    'circle': lambda radius: math.pi * radius ** 2
}

def calculate_area(shape, *dimensions):
    return SHAPE_FORMULAS[shape](*dimensions)

def compare_areas(length, width, radius):
    rectangle_area = calculate_area('rectangle', length, width)
    circle_area = calculate_area('circle', radius)
    print(f"Rectangle Area: {rectangle_area:.2f}")
    print(f"Circle Area: {circle_area:.2f}")

if __name__ == '__main__':
    sample_values = {
        'length': 5.0,
        'width': 3.0,
        'radius': 4.0
    }
    compare_areas(sample_values['length'], sample_values['width'], sample_values['radius'])