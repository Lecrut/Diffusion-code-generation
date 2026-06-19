class Square:
    def __init__(self, side_length):
        """Initialize a Square with a given side length."""
        self.side = side_length
    
    @property
    def area(self) -> float:
        """Calculate and return the square's area based on its side length.
        
        Returns:
            The calculated area of the square (side ** 2).
        """
        return self.side * self.side

if __name__ == '__main__':
    # Sample values for testing without user input or network access
    sample_side = 5
    
    try:
        side_length = float(sample_side)
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        
        square = Square(side_length)
        print(f"Square with side {square.side} has an area of {square.area}")
    except Exception as e:
        print(f"Error creating Square object: {e}")