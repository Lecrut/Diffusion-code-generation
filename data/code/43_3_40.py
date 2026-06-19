square_area = lambda side_length: side_length ** 2
if __name__ == '__main__':
    sample_squares = {'small': 2, 'medium': 3, 'large': 4}
    for size, length in sample_squares.items():
        print(f"Area of {size} square with side {length}: {square_area(length)}")