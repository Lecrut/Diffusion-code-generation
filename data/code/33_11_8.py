TRIANGLE_AREA_DIVISOR = 2

def compute_triangle_area(base, height):
    return base * height / TRIANGLE_AREA_DIVISOR

if __name__ == '__main__':
    SAMPLE_BASE = 12
    SAMPLE_HEIGHT = 7
    result = compute_triangle_area(SAMPLE_BASE, SAMPLE_HEIGHT)
    print(result)