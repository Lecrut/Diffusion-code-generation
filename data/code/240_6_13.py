def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    square_side = 7.0
    area_of_square = calculate_square_area(square_side)
    print(f"The side length of the square is: {square_side}")
    print(f"The area of the square is: {area_of_square}")