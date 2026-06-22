AREA_MULTIPLIER = 0.5

def compute_triangle_area(base_value, height_value):
    if base_value <= 0 or height_value <= 0:
        raise ValueError("Base and height must be positive values")
    return base_value * height_value * AREA_MULTIPLIER

if __name__ == '__main__':
    SAMPLE_BASE = 14.75
    SAMPLE_HEIGHT = 8.25
    result = compute_triangle_area(SAMPLE_BASE, SAMPLE_HEIGHT)
    print(result)