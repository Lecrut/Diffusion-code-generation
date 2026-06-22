import math

def calculate_area(shape_type, **kwargs):
    shape_type = shape_type.lower()
    if shape_type == 'rectangle':
        length = kwargs.get('length')
        width = kwargs.get('width')
        if length is None or width is None:
            raise ValueError("Rectangle requires 'length' and 'width' dimensions.")
        return length * width
    elif shape_type == 'circle':
        radius = kwargs.get('radius')
        if radius is None:
            raise ValueError("Circle requires 'radius' dimension.")
        return math.pi * (radius ** 2)
    else:
        raise ValueError("Unsupported shape type. Use 'rectangle' or 'circle'.")

if __name__ == '__main__':
    rect_area = calculate_area('rectangle', length=5, width=3)
    print(rect_area)

    circle_area = calculate_area('circle', radius=4)
    print(circle_area)