def compute_triangle_area(base, height):
    if base <= 0:
        return 0.0
    if height <= 0:
        return 0.0
    return 0.5 * base * height

if __name__ == '__main__':
    base_value = 7.0
    height_value = 3.5
    computed_result = compute_triangle_area(base_value, height_value)
    print(computed_result)