def calculate_square_area(side_length):
    return side_length ** 2

if __name__ == '__main__':
    sample_squares = {
        'small': 3,
        'medium': 4,
        'large': 5
    }
    for size, side in sample_squares.items():
        area = calculate_square_area(side)
        print(f"The area of the {size} square is: {area}")