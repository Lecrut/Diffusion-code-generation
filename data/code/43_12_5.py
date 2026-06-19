class Square:
    def __init__(self, side_length):
        """
        Initialize a Square object with the given side length.
        
        Args:
            side_length (float or int): The length of one side of the square.
                                      Must be non-negative.
        Raises:
            ValueError: If the side length is negative.
        """
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        
        self._side = side_length
    
    def get_area(self):
        """
        Calculate and return the area of the square.
        
        Returns:
            float: The calculated area (side * side).
        """
        return self._side ** 2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    try:
        # Create instances with different sizes
        small_square = Square(5)
        medium_square = Square(-3.0)

        print(f"Area of square with side 5: {small_square.get_area()}")

        # This will raise an exception as expected since -3 is invalid
        area_of_medium = medium_square.get_area()
    except ValueError as e:
        print(f"Error creating or using the second square object: {e}")
    
    # Correct usage for a larger square side
    large_square = Square(10)
    print(f"Area of large square with side 10: {large_square.get_area()}")