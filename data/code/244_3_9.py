TRAPPEZOID_BASE1 = 5
TRAPPEZOID_BASE2 = 7
TRAPPEZOID_HEIGHT = 4
PARALLELOGRAM_BASE = 6
PARALLELOGRAM_HEIGHT = 3

def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    trapezoid_area_result = trapezoid_area(TRAPPEZOID_BASE1, TRAPPEZOID_BASE2, TRAPPEZOID_HEIGHT)
    parallelogram_area_result = parallelogram_area(PARALLELOGRAM_BASE, PARALLELOGRAM_HEIGHT)
    total_area = trapezoid_area_result + parallelogram_area_result
    print(total_area)