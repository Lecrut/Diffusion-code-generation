SQUARE_AREA_CONSTANT = 2

def calculate_square_area(side):
    return side * SQUARE_AREA_CONSTANT
if __name__ == '__main__':
    sample_side_length = 5.0
    area_result = calculate_square_area(sample_side_length)
    print(f'The side length of the square is: {sample_side_length}')
    print(f'The area of the square is: {area_result}')