def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    SQUARE_SIDE_LENGTH = 5.0
    area = calculate_square_area(SQUARE_SIDE_LENGTH)
    print(f"The side length of the square is: {SQUARE_SIDE_LENGTH}")
    print(f"The area of the square is: {area}")