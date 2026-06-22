def calculate_rhombus_area(diagonal_a, diagonal_b):
    return (diagonal_a * diagonal_b) / 2

if __name__ == '__main__':
    d1 = 10
    d2 = 15
    result = calculate_rhombus_area(d1, d2)
    print(result)