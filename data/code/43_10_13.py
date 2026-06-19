class SquareCalculator:
    def __init__(self, side_length):
        self.side_length = float(side_length) if isinstance(self.side_length, str) else self.side_length
    
    def calculate_area(self):
        return self.side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or network access
    side_lengths = [5.0, '10', 3]

    for length in side_lengths:
        try:
            calculator = SquareCalculator(length)
            area = calculator.calculate_area()
            print(f"Square with side {length} has an area of {area}")
        except ValueError as e:
            # Gracefully handle potential input conversion errors if a string is passed incorrectly
            print(f"Error processing value '{length}': {e}")