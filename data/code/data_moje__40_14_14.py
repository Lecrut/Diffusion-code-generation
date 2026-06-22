from typing import Final

DIMENSIONS: Final[tuple[float, float, float]] = (2.5, 3.0, 4.0)

def compute_rectangular_box_surface_area(length: float, width: float, height: float) -> float:
    face_one: float = length * width
    face_two: float = width * height
    face_three: float = length * height
    total_area: float = 2 * (face_one + face_two + face_three)
    return total_area

if __name__ == '__main__':
    dim_length: float = DIMENSIONS[0]
    dim_width: float = DIMENSIONS[1]
    dim_height: float = DIMENSIONS[2]
    surface: float = compute_rectangular_box_surface_area(dim_length, dim_width, dim_height)
    print(surface)