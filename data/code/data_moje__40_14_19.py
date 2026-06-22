from typing import List

def compute_box_surface_area(dimensions: List[float]) -> float:
    l: float = dimensions[0]
    w: float = dimensions[1]
    h: float = dimensions[2]
    area_ab: float = l * w
    area_bc: float = w * h
    area_ca: float = h * l
    total: float = 2 * (area_ab + area_bc + area_ca)
    return total

if __name__ == '__main__':
    input_dimensions: List[float] = [2.5, 3.0, 4.0]
    calculated_value: float = compute_box_surface_area(input_dimensions)
    print(calculated_value)