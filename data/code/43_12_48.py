class Square:
    def __init__(self, side_length):
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_squares = {
        'tiny': Square(1),
        'small': Square(3),
        'medium': Square(5),
        'large': Square(7)
    }
    
    for size, square in sample_squares.items():
        print(f"The area of the {size} square is {square.area()}")