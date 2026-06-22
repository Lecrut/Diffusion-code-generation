def compute_triangle_area(base: float, height: float) -> float:
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Base and height must be numeric")
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive")
    return float(base * height) / 2.0

if __name__ == '__main__':
    _BASE = 12.5
    _HEIGHT = 4.0
    result = compute_triangle_area(_BASE, _HEIGHT)
    print(result)