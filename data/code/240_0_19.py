SQUARE_SIDES = 4

def calculate_square_area(side_length):
    return side_length ** SQUARE_SIDES

if __name__ == '__main__':
    sample_side_length = 5
    area = calculate_square_area(sample_side_length)
    print(f"The area of the square with side length {sample_side_length} is: {area}")