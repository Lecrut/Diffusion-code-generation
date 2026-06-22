def calculate_rhombus_area(diagonal_one, diagonal_two):
    return 0.5 * diagonal_one * diagonal_two

if __name__ == '__main__':
    d1 = 10
    d2 = 24
    result = calculate_rhombus_area(d1, d2)
    print(result)