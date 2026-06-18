class Square:
    def __init__(self, side_length):
        """Initialize a Square with a given side length."""
        if side_length < 0:
            raise ValueError("Side length cannot be negative.")
        self.side_length = side_length
    
    def calculate_area(self) -> float:
        """Calculate and return the area of the square."""
        return self.side_length ** 2

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    sample_side = 5.0

    try:
        square_instance = Square(sample_side)
        calculated_area = square_instance.calculate_area()
        
        print(f"Square with side length {sample_side}")
        print(f"Area: {calculated_area}")
    except ValueError as e:
        print(f"Error creating Square instance: {e}")