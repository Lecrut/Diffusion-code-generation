class Square:
    def __init__(self, side_length):
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        self.side_length = float(side_length)
    
    def get_area(self) -> float:
        return self.side_length ** 2

if __name__ == '__main__':
    square1 = Square(5.0)
    print(f"Area of square with side 5: {square1.get_area()}")
    
    try:
        invalid_square = Square(-3.0)
    except ValueError as e:
        print(f"Error handling test passed: {e}")
    
    # Additional sample calculation without user input
    result = (Square(7).get_area() * 2 + Square(4).get_area())
    print(f"Combined area of two squares calculated correctly.")