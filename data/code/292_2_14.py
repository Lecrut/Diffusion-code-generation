def compute_herons_formula(a, b, c):
    semi_perimeter = (a + b + c) / 2
    area_squared = semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)
    return area_squared ** 0.5

if __name__ == '__main__':
    side_a = 6
    side_b = 8
    side_c = 10
    result = compute_herons_formula(side_a, side_b, side_c)
    print(result)