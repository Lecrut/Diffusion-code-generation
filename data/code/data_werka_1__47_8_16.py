def calculate_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    sample_values = {
        'base': 12,
        'height': 8
    }
    area_result = calculate_triangle_area(sample_values['base'], sample_values['height'])
    print(area_result)