SQUARE_AREA_CONSTANT = 2

def calculate_square_area(side_length):
    return side_length ** SQUARE_AREA_CONSTANT

if __name__ == '__main__':
    sample_side = 5
    result = calculate_square_area(sample_side)
    print(f"The area of a square with side {sample_side} is: {result}")