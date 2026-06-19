from typing import Tuple

def calculate_area(length: float, width: float) -> float:
    return length * width

if __name__ == '__main__':
    shape_dimensions = {
        'rectangle': (10.0, 5.0),
        'square': (6.0, 6.0)
    }
    
    for shape, dimensions in shape_dimensions.items():
        area = calculate_area(*dimensions)
        print(f"Area of {shape} with dimensions {dimensions}: {area}")