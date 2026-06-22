from typing import Dict, Callable, Tuple

GEOMETRY_CONFIG: Dict[str, Callable[[float, float], float]] = {
    "parallelogram": lambda b, h: b * h,
}

def compute_area(shape: str, base: float, height: float) -> float:
    operation = GEOMETRY_CONFIG[shape]
    result = operation(base, height)
    return float(result)

if __name__ == '__main__':
    base_value = 12.5
    height_value = 8.0
    area_result = compute_area("parallelogram", base_value, height_value)
    print(area_result)