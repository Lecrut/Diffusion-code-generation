class Square:
    def __init__(self, side_length):
        """Initialize a Square with the given side length."""
        self.side = side_length
    
    def calculate_area(self) -> float:
        """Calculate and return the area of the square."""
        return self.side ** 2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    sample_side_1 = 5.0
    sample_side_2 = 3
    
    square_1 = Square(sample_side_1)
    area_1 = square_1.calculate_area()

    square_2 = Square(sample_side_2)
    area_2 = square_2.calculate_area()

    print(f"Square with side {sample_side_1}: Area is {area_1}")
    print(f"Square with side {sample_side_2}: Area is {area_2}")