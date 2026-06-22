def compute_rhombus_area(diagonal1, diagonal2):
    half = 0.5
    product = diagonal1 * diagonal2
    return half * product

if __name__ == '__main__':
    diagonal_one = 12
    diagonal_two = 8
    calculated_area = compute_rhombus_area(diagonal_one, diagonal_two)
    print(calculated_area)