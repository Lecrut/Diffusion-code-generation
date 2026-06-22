def calculate_kite_perimeter(side_a, side_b):
    return 2 * (side_a + side_b)

if __name__ == '__main__':
    perimeter = calculate_kite_perimeter(5, 7)
    print(perimeter)