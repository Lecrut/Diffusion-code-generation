class Number:
    """A class representing a number with comparison capabilities."""
    
    def __init__(self, value):
        """Initialize the Number object with an integer or float value."""
        self.value = int(value) if isinstance(value, (float,)) else value
        
    def compare_to(self, other_number: 'Number') -> bool:
        """Compare this number against another passed as a method argument.
        
        Args:
            other_number: Another Number object to compare against.
            
        Returns:
            True if self is greater than or equal to other_number, False otherwise.
        """
        return self.value >= other_number.value

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input needed)
    
    num1 = Number(50)
    num2 = Number(30)
    num3 = Number(60)
    
    print(f"Comparing {num1.value} vs {num2.value}:")
    result_a = num1.compare_to(num2)
    print(f"{num1.value} >= {num2.value}? Result: {result_a}")  # True
    
    print(f"\nComparing {num3.value} vs {num2.value}:")
    result_b = num3.compare_to(num2)
    print(f"{num3.value} >= {num2.value}? Result: {result_b}")  # True

    print(f"\nComparing {num1.value} vs {num3.value}:")
    result_c = num1.compare_to(num3)
    print(f"{num1.value} >= {num3.value}? Result: {result_c}")  # False
    
    assert result_a == True, "Assertion failed for first comparison"
    assert result_b == True, "Assertion failed for second comparison"
    assert result_c == False, "Assertion failed for third comparison"
    
    print("\nAll comparisons executed successfully.")