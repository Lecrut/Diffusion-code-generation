"""
Utility module containing a static method to check if a number is negative.
Adheres strictly to Pythonic style guidelines (PEP 8).
No external dependencies or interactive input required.
"""

class NumberChecker:
    """A utility class for basic numerical checks."""

    @staticmethod
    def is_negative(value):
        """
        Check if the given value is negative.

        Args:
            value (int | float): The number to check.

        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access.
    test_values = [
        -5,      # Should be negative
        0,       # Not negative (zero)
        3.14,    # Positive float
        None,    # Will raise TypeError as per Pythonic behavior for type checking logic usually implied here if not handled explicitly by caller, but strictly 'is_negative' checks value < 0 which fails on non-numeric types in a way that raises error or returns False depending on strictness. 
                # To be purely functional and safe without side effects:
        -10      # Negative integer
    ]

    print("Testing NumberChecker.is_negative():")
    for val in test_values[3:]:  # Skip None to avoid TypeError during < comparison if not handled, demonstrating robustness. 
                                # Actually, let's include a safe check or just run on valid numbers to keep it simple and runnable as requested without complex error handling unless asked.
        pass

    results = []
    for val in [-5, 0, 3.14]:
        result = NumberChecker.is_negative(val)
        print(f"is_negative({val}) -> {result}")

    # Demonstration with a negative value specifically requested by logic flow above to show success case clearly if needed, 
    # but the loop covers -5 which is sufficient.