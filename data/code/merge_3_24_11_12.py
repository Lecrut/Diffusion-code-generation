class NumberChecker:
    def check_negativity(self, value):
        """
        Determines if the input value is negative.
        
        Args:
            value (int or float): The number to check.
            
        Returns:
            bool: True if the value is strictly less than zero, False otherwise.
        """
        return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample test cases with hard-coded values
    samples = [
        -5,      # Negative integer -> True
        -3.14,   # Negative float -> True
        0,       # Zero -> False (not negative)
        42,      # Positive int -> False
        0.0,     # Zero float -> False
    ]

    for sample in samples:
        result = checker.check_negativity(sample)
        print(f"check_negativity({sample}) = {result}")