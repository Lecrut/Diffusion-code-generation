def compute_square_area(side):
    return side * side

if __name__ == '__main__':
    sample_squares = {'small': 2, 'medium': 4, 'large': 6}
    for description, side in sample_squares.items():
        print(f"The area of the {description} square is: {compute_square_area(side)}")