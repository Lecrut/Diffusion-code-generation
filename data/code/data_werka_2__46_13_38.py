def calculate_perimeter(side_a, side_b, side_c):
    return side_a + side_b + side_c

if __name__ == '__main__':
    side_length1 = 9
    side_length2 = 12
    side_length3 = 15
    perimeter_value = calculate_perimeter(side_length1, side_length2, side_length3)
    print(perimeter_value)