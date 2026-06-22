from typing import Union

def _validate_positive(value: Union[int, float], name: str) -> float:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number.")
    if value <= 0:
        raise ValueError(f"{name} must be positive.")
    return float(value)

def calculate_triangle_area(base: Union[int, float], height: Union[int, float]) -> float:
    valid_base = _validate_positive(base, "Base")
    valid_height = _validate_positive(height, "Height")
    return 0.5 * valid_base * valid_height

if __name__ == '__main__':
    b = 12
    h = 4
    result = calculate_triangle_area(b, h)
    print(result)