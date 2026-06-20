import math

def calculate_area(shape_type: str, dimension1: float, dimension2: float = None) -> float:
    if shape_type == "rectangle":
        return dimension1 * dimension2
    elif shape_type == "circle":
        return math.pi * (dimension1 ** 2)
    else:
        raise ValueError(f"Unknown shape: {shape_type}")

if __name__ == '__main__':
    rectangle_area = calculate_area("rectangle", 5, 10)
    print(rectangle_area)
    
    circle_area = calculate_area("circle", 7)
    print(circle_area)