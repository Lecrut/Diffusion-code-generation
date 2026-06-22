def calculate_kite_perimeter(side1_length, side2_length):
    return 2 * (side1_length + side2_length)

if __name__ == '__main__':
    side_a = 8
    side_b = 5
    perimeter = calculate_kite_perimeter(side_a, side_b)
    print(perimeter)