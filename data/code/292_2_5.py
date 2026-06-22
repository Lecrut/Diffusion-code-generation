def compute_herons_formula(a, b, c):
    semi_perimeter = (a + b + c) / 2
    area_squared = semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)
    return area_squared ** 0.5

if __name__ == '__main__':
    side1 = 7
    side2 = 24
    side3 = 25
    perimeter = compute_herons_formula(side1, side2, side3)
    print(perimeter)