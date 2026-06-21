SHAPES_AREA_FORMULAS = {
    'square': lambda side: side * side,
    'rectangle': lambda length, width: length * width,
}

def calculate_square_area(side_length):
    area_formula = SHAPES_AREA_FORMULAS['square']
    return area_formula(side_length)

if __name__ == '__main__':
    side = 50
    area = calculate_square_area(side)
    print(area)