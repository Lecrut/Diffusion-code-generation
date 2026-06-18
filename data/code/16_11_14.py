class NumberChecker:
    """A class to check numerical properties."""

    def __init__(self):
        pass

    def check_positivity(self, value) -> bool:
        """
        Determines if the provided numeric value is positive (greater than zero).

        Args:
            value (number): The number to evaluate.

        Returns:
            bool: True if value > 0, False otherwise.
        """
        return isinstance(value, (int, float)) and value > 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Hard-coded sample values running without user input or external resources
    test_values = [5, -3, 0, "10", True]

    print("Testing positivity checks:")
    for val in test_values:
        result = checker.check_positivity(val)
        status = "Positive" if result else "Not Positive"
        try:
            display_val = repr(val)
        except Exception as e:
            display_val = f"<Error processing {val}>"

        print(f"{display_val}: -> ({status})")