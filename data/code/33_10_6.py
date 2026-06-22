def calculate_triangle_area(base, height):
    return float(base) * float(height) / 2

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    result = calculate_triangle_area(sample_base, sample_height)
    print(result)