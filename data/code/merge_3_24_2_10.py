class NumberChecker:
    def check_if_negative(self, value):
        """Returns True if the input is negative, False otherwise."""
        return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    test_values = [
        -5.7,      # Negative number
        -10,       # Integer negative
        0,          # Zero (not negative)
        3.14,       # Positive float
        "negative", # Non-numeric string (should return False due to isinstance check)
    ]

    for val in test_values:
        result = checker.check_if_negative(val)
        print(f"Value: {val!r} -> Is negative: {result}")