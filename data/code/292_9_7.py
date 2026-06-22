def calculate_kite_perimeter(side_a, side_b):
    return 2 * (side_a + side_b)

if __name__ == '__main__':
    side_length1 = 8
    side_length2 = 6
    perimeter = calculate_kite_perimeter(side_length1, side_length2)
    print(perimeter)