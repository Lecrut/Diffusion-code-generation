SQUARE_AREA_FACTOR = 2

def calculate_square_area(side_length):
    return side_length * side_length * SQUARE_AREA_FACTOR

if __name__ == '__main__':
    sample_side_lengths = [2, 4, 6]
    for side in sample_side_lengths:
        area = calculate_square_area(side)
        print(f"The area of the square with side length {side} is: {area}")