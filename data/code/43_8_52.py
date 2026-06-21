SQUARE_AREA_MULTIPLIER = 2

def calculate_square_area(side):
    return side * SQUARE_AREA_MULTIPLIER

if __name__ == '__main__':
    sample_side_length = 5
    print(calculate_square_area(sample_side_length))