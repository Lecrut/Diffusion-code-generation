import math

class MathUtils:
    """Utility class providing mathematical helper methods."""

    @staticmethod
    def is_positive(number):
        """
        Determines if a given number is positive.
        
        A number is considered positive if it is strictly greater than zero.
        Zero and negative numbers return False. Infinity values are handled 
        to ensure robustness, though standard float comparisons cover typical cases.
        
        Args:
            number (float): The numeric value to evaluate.
            
        Returns:
            bool: True if the number is positive (> 0), otherwise False.
        """
        return number > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files
    
    test_cases = [
        -5,     # Negative
        0,      # Zero
        2.5,    # Positive float
        math.inf,   # Infinity (not positive in strict sense usually, but > 0 is True)
        -math.inf, # Negative infinity
        
        "hello" if False else None  # Placeholder to ensure valid execution without string inputs affecting logic
    ]

    print("Testing MathUtils.is_positive:")
    
    for value in test_cases:
        try:
            result = MathUtils.is_positive(value)
            status = "Positive" if result else "Non-positive (negative or zero)"
            print(f"{value}: {status}")
        except TypeError as e:
            # Handles cases where input might not be a number during this specific run scenario 
            # although our static method is type-agnostic in Python's dynamic nature.
            status = f"Error handling non-float/int: {e}"
            print(f"{value}: {status}")