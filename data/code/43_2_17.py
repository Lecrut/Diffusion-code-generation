class Square:
    def __init__(self, side_length):
        """Initialize a Square with the given side length."""
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        self.side = float(side_length)

    def area(self):
        """Calculate and return the area of the square."""
        return self.side ** 2

if __name__ == '__main__':
    # Sample values to demonstrate functionality without user input
    side_a = 5.0
    side_b = -3.0

    try:
        sq1 = Square(side_a)
        print(f"Square with side {side_a}: Area is {sq1.area()}")
        
        try:
            sq2 = Square(side_b)
        except ValueError as e:
            print(f"Error creating square with negative side: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")