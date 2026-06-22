def calculate_rhombus_area(diagonal_one, diagonal_two):
    return (diagonal_one * diagonal_two) / 2

if __name__ == '__main__':
    diagonal_a = 10
    diagonal_b = 15
    area = calculate_rhombus_area(diagonal_a, diagonal_b)
    print(area)