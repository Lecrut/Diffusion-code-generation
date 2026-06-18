class Square:
    """A class representing a square with methods to calculate its area."""

    def __init__(self, side_length):
        """
        Initialize the Square object with a given side length.

        Args:
            side_length (float or int): The length of one side of the square.
        
        Raises:
            ValueError: If side_length is negative.
        """
        if not isinstance(side_length, (int, float)):
            raise TypeError("side_length must be a number")
        self.side = side_length

    def get_area(self):
        """
        Calculate and return the area of the square.

        Returns:
            float or int: The calculated area of the square.
        
        Raises:
            ValueError: If side is negative (though prevented in constructor).
        """
        if self.side < 0:
            raise ValueError("Side length cannot be negative.")
        return self.side ** 2

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without external input.
    try:
        side_a = Square(5)
        print(f"Square with side {side_a.side} has area: {side_a.get_area()}")

        side_b = Square(-2)  # This will raise an error to demonstrate validation logic if not caught elsewhere, 
                            # but here we let the constructor handle it. The constructor should ideally catch this before assignment or allow negative sides depending on domain rules.
                            # Re-implementing based on typical geometric constraints where side must be non-negative:

        try:
            invalid_square = Square(-2)
        except ValueError as ve:
            print(f"Error creating square with -2: {ve}")

    except Exception as e:
        print(f"An error occurred during sample execution: {e}")