RHOMBUS_AREA_FORMULA = lambda d1, d2: 0.5 * d1 * d2
SQUARE_AREA_FORMULA = lambda side: side ** 2

def compare_areas(d1, d2, side):
    rhombus_area = RHOMBUS_AREA_FORMULA(d1, d2)
    square_area = SQUARE_AREA_FORMULA(side)
    return {
        "rhombus_area": rhombus_area,
        "square_area": square_area,
        "difference": rhombus_area - square_area
    }

if __name__ == '__main__':
    result = compare_areas(10, 8, 6)
    print(f"Rhombus Area: {result['rhombus_area']}")
    print(f"Square Area: {result['square_area']}")
    print(f"Difference: {result['difference']}")