def calculate_rhombus_area(diagonal_one, diagonal_two):
    return (diagonal_one * diagonal_two) / 2.0

if __name__ == '__main__':
    d1 = 10
    d2 = 14
    result = calculate_rhombus_area(d1, d2)
    print(result)