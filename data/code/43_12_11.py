class Square:
    """A class representing a square with methods to calculate its area."""
    
    def __init__(self, side_length):
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length must be an integer or float")
        self.side = side_length
    
    def get_area(self):
        """Calculate and return the square's area.
        
        Returns:
            float: The calculated area of the square.
        """
        return self.side ** 2

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    sample_sides = [5, 10.5]

    print("Square Area Calculations:")
    for side in sample_sides:
        square = Square(side)
        area = square.get_area()
        print(f"Side length: {side}, Area: {area}")