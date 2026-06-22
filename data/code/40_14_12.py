from typing import NamedTuple

class Dimensions(NamedTuple):
    length: float
    width: float
    height: float

def _validate_positive(value: float, name: str) -> float:
    if value <= 0:
        raise ValueError(f"{name} must be positive, got {value}")
    return value

def compute_rectangular_surface_area(dim: Dimensions) -> float:
    l: float = _validate_positive(dim.length, "length")
    w: float = _validate_positive(dim.width, "width")
    h: float = _validate_positive(dim.height, "height")
    
    face_area_top_bottom: float = l * w
    face_area_front_back: float = w * h
    face_area_left_right: float = h * l
    
    total_surface_area: float = 2 * (face_area_top_bottom + face_area_front_back + face_area_left_right)
    return total_surface_area

if __name__ == '__main__':
    input_dimensions: Dimensions = Dimensions(length=2.5, width=3.0, height=4.0)
    calculated_area: float = compute_rectangular_surface_area(input_dimensions)
    print(calculated_area)