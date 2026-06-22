def _ensure_numeric(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be numeric")
    return value

def calculate_parallelogram_area(base, height):
    base = _ensure_numeric(base, "base")
    height = _ensure_numeric(height, "height")
    return base * height

if __name__ == '__main__':
    SAMPLE_BASE = 12.5
    SAMPLE_HEIGHT = 4.8
    area = calculate_parallelogram_area(SAMPLE_BASE, SAMPLE_HEIGHT)
    print(area)