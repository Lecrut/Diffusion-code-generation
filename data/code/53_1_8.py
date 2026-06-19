class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    sample_squares = {
        'small': 3,
        'medium': 5,
        'large': 7
    }
    
    square_size = sample_squares['medium']
    square = Square(square_size)
    print(f"The area of a square with side length {square.side_length} is {square.area()}")