TRIANGLE_AREA_COEFFICIENT = 0.5

def calculate_triangle_area(base_length: float, vertical_height: float) -> float:
    product = base_length * vertical_height
    return product * TRIANGLE_AREA_COEFFICIENT

if __name__ == '__main__':
    sample_base = 12.5
    sample_height = 8.0
    final_area = calculate_triangle_area(sample_base, sample_height)
    print(final_area)