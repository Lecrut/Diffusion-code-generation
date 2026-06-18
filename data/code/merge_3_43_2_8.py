class Square:
    def __init__(self, side_length):
        """Initialize a Square with a given positive side length."""
        if side_length <= 0:
            raise ValueError("Side length must be greater than zero.")
        self._side = side_length
    
    @property
    def area(self) -> float:
        """Calculate and return the area of the square."""
        return self._side ** 2

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input.
    try:
        sq1 = Square(5)
        print(f"Area with side length {sq1._side}: {sq1.area}")
        
        # Test edge case handling implicitly by not calling it, 
        # but we can demonstrate valid positive cases.
        sides = [3.0, 4]
        for s in sides:
            sq2 = Square(s)
            print(f"Area with side length {s}: {sq2.area}")
    except ValueError as ve:
        print(f"Error occurred: {ve}")