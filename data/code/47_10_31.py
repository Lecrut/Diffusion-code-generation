def compute_triangle_area(base_length, height_length):
    if base_length <= 0 or height_length <= 0:
        raise ValueError("Base and height must be positive numbers.")
    area = 0.5 * base_length * height_length
    return area

if __name__ == '__main__':
    SAMPLE_BASE = 6
    SAMPLE_HEIGHT = 4
    try:
        computed_area = compute_triangle_area(SAMPLE_BASE, SAMPLE_HEIGHT)
        print(computed_area)
    except ValueError as e:
        print(e)