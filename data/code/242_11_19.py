SHAPES = {
    'square': lambda side: side ** 2,
    'triangle': lambda base, height: 0.5 * base * height
}

def compare_areas():
    side_length_square = 5
    base_triangle = 4
    height_triangle = 6
    area_square = SHAPES['square'](side_length_square)
    area_triangle = SHAPES['triangle'](base_triangle, height_triangle)
    return area_square > area_triangle

if __name__ == '__main__':
    print(compare_areas())