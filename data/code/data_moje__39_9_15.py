def _validate_dimensions(value: float, name: str) -> None:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    if value <= 0:
        raise ValueError(f"{name} must be positive")

def calculate_prism_volume() -> float:
    base_area: float = 15.0
    height: float = 7.5
    _validate_dimensions(base_area, "base_area")
    _validate_dimensions(height, "height")
    return base_area * height

if __name__ == '__main__':
    volume_result = calculate_prism_volume()
    print(volume_result)