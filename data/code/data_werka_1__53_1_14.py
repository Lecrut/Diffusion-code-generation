class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

if __name__ == '__main__':
    side_value = 7
    square = Square(side_value)
    print(f"Area of the square with side length {side_value}: {square.area()}")
    
    another_side_value = 10
    another_square = Square(another_side_value)
    print(f"Area of another square with side length {another_side_value}: {another_square.area()}")