SQUARE_SIDES = 4

def calculate_square_perimeter(side_length):
    return SQUARE_SIDES * side_length

if __name__ == '__main__':
    side_length = 9
    perimeter = calculate_square_perimeter(side_length)
    print(perimeter)