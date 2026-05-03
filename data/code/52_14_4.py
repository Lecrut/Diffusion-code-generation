import math
def calculate_area(shape, **kwargs):
    if shape == "rectangle":
        length = kwargs.get("length")
        width = kwargs.get("width")
        if length is not None and width is not None:
            return length * width
        else:
            raise ValueError("Rectangle requires 'length' and 'width'")
    elif shape == "circle":
        radius = kwargs.get("radius")
        if radius is not None:
            return math.pi * (radius ** 2)
        else:
            raise ValueError("Circle requires 'radius'")
    elif shape == "triangle":
        base = kwargs.get("base")
        height = kwargs.get("height")
        if base is not None and height is not None:
            return 0.5 * base * height
        else:
            raise ValueError("Triangle requires 'base' and 'height'")
    else:
        raise ValueError(f"Invalid shape type: {shape}")
if __name__ == '__main__':
    print(f"Rectangle Area: {calculate_area('rectangle', length=10, width=5)}")
    print(f"Circle Area: {calculate_area('circle', radius=4)}")
    print(f"Triangle Area: {calculate_area('triangle', base=8, height=4)}")
    try:
        calculate_area('square', side=5)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        calculate_area('circle', radius=2)
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        calculate_area('rectangle', length=10)
    except ValueError as e:
        print(f"Error caught: {e}")