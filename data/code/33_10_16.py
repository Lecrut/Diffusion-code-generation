def calculate_triangle_area(base, height):
    return (base * height) / 2

if __name__ == '__main__':
    sample_base = 10.0
    sample_height = 5.5
    result = calculate_triangle_area(sample_base, sample_height)
    print(result)