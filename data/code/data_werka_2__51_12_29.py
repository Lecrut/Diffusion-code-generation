SQUARE_SIDES = 4

def calculate_perimeter(side_length):
    return SQUARE_SIDES * side_length

if __name__ == '__main__':
    sample_side_length = 9
    perimeter = calculate_perimeter(sample_side_length)
    print(perimeter)