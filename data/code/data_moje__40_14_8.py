from typing import List, Tuple

DIMENSIONS_CONFIG: Tuple[float, ...] = (2.5, 3.0, 4.0)
FACE_PAIRS: dict = {
    "xy": 0,
    "yz": 1,
    "zx": 2,
}

def get_face_area(dimensions: Tuple[float, float, float], axis_pair: str) -> float:
    if axis_pair == "xy":
        return dimensions[0] * dimensions[1]
    if axis_pair == "yz":
        return dimensions[1] * dimensions[2]
    return dimensions[2] * dimensions[0]

def compute_box_surface_area(dims: Tuple[float, float, float]) -> float:
    areas: List[float] = []
    for key in FACE_PAIRS:
        areas.append(get_face_area(dims, key))
    return sum(areas) * 2

if __name__ == "__main__":
    d1: float = DIMENSIONS_CONFIG[0]
    d2: float = DIMENSIONS_CONFIG[1]
    d3: float = DIMENSIONS_CONFIG[2]
    length: float = d1
    width: float = d2
    height: float = d3
    total_area: float = compute_box_surface_area((length, width, height))
    print(total_area)