import math

def calculate_area(shape_type, dimension1, dimension2=None):
    shape_type_lower = shape_type.lower().strip()
    if shape_type_lower == 'rectangle':
        width = dimension1
        height = dimension2
        area = width * height
    elif shape_type_lower == 'circle':
        radius = dimension1
        area = math.pi * (radius ** 2)
    else:
        area = 0
    return area

if __name__ == '__main__':
    rect_area = calculate_area('rectangle', 5, 10)
    print(rect_area)
    
    circle_area = calculate_area('circle', 7)
    print(circle_area)