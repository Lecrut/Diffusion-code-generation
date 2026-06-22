SQUARE_SIDES = 4

def calculate_perimeter(side_length):
    return SQUARE_SIDES * side_length

if __name__ == '__main__':
    side_length = 12
    perimeter = calculate_perimeter(side_length)
    print(perimeter)