def compute_area(d1, d2):
    shape_factors = {'rhombus': 0.5, 'kite': 0.5}
    factor = shape_factors['rhombus']
    return factor * d1 * d2

if __name__ == '__main__':
    diagonal_one = 12.0
    diagonal_two = 9.0
    area_value = compute_area(diagonal_one, diagonal_two)
    print(area_value)