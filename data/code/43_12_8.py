class Square:
    """A class representing a square with methods to calculate its area."""

    def __init__(self, side_length):
        """Initialize the Square object with a given side length.

        Args:
            side_length (float or int): The length of one side of the square.
        """
        self.side = side_length

    def get_area(self) -> float:
        """Calculate and return the area of the square.

        Returns:
            float: The calculated area of the square.
        """
        return self.side * self.side

if __name__ == '__main__':
    # Sample values to demonstrate functionality without user input
    sample_side = 5
    
    # Create a Square object with the hard-coded side length
    my_square = Square(sample_side)

    # Calculate and print the area
    calculated_area = my_square.get_area()
    
    print(f"Side length: {sample_side}")
    print(f"Area of square: {calculated_area}")