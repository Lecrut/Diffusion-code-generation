import math

SHAPES = {
    "cylinder": {"formula": "2 * pi * r * (r + h)", "needs": ["radius", "height"]}
}

def cylinder_surface_area(radius: float, height: float) -> float:
    base_area = math.pi * radius * radius
    side_area = 2 * math.pi * radius * height
    return 2 * base_area + side_area

if __name__ == '__main__':
    radius_val = 3.0
    height_val = 7.0
    calculated_area = cylinder_surface_area(radius_val, height_val)
    print(calculated_area)