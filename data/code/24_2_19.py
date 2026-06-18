class NumberChecker:
    def check_if_negative(self, value):
        """
        Determines if the input value is negative.
        
        Args:
            value (int or float): The numerical value to check.
            
        Returns:
            bool: True if the value is strictly less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [
        -5,      # Negative
        0,       # Zero (not negative)
        3.14,    # Positive float
        -3e-2,   # Small negative number in scientific notation
        "abc",   # Invalid input type demonstration (will raise TypeError as expected for strict checking or handled gracefully if needed; here we assume numeric context per task implication but strictly < works on strings by returning False due to lexicographical comparison which might be unintended. To ensure robustness purely based on 'negative' definition usually implying numbers, let's rely only on int/float in main block as typical OOP usage).
    ]

    # Correcting the test_values list to exclude non-numeric types that complicate "negativity" check unless explicitly cast
    numeric_samples = [-10, 0.5, -3e2] 

    for val in numeric_samples:
        result = checker.check_if_negative(val)
        print(f"Value {val} is negative? {result}")

    # Demonstrate with a generic unknown type to show behavior (optional extension if desired, 
    # but sticking to strict numerical logic as per 'negative' definition usually implies numbers.
    # The above loop covers the requirement cleanly.)