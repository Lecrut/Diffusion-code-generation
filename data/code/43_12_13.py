class Square:
    def __init__(self, side_length):
        """Initialize a Square with the given side length."""
        self.side_length = side_length
    
    def area(self) -> float:
        """Calculate and return the square's area based on its side length.
        
        Returns:
            The calculated area as a float.
        """
        return self.side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [5, -3, 0]

    print("Square Area Calculations:")
    for side in test_cases:
        try:
            square = Square(side)
            area_result = square.area()
            print(f"Side length {side}: Area is {area_result}")
        except ValueError as e:
            # Handle invalid input gracefully (e.g., negative lengths if strictly enforced, 
            # though the task doesn't specify validation rules explicitly. Python allows negatives mathematically).
            pass

    # Demonstration with a positive integer for clarity
    sample_square = Square(10)
    print(f"\nSample: A square with side 10 has an area of {sample_square.area()}")