def compute_square_area(side):
    return side ** 2

if __name__ == '__main__':
    sample_squares = {'small': 4, 'medium': 6, 'large': 8}
    for size, side in sample_squares.items():
        print(f"The area of the {size} square is: {compute_square_area(side)}")