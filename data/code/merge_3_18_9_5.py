class Number:
    """A class representing a number with comparison capabilities."""
    
    def __init__(self, value):
        """Initialize the Number object with an integer or float value."""
        self.value = int(value) if isinstance(value, (int, float)) else value
    
    def compare(self, other_number: 'Number') -> bool:
        """Compare this number against another passed as a Number argument.
        
        Args:
            other_number: Another Number object to compare against.
            
        Returns:
            True if self.value is less than or equal to other_number's value, False otherwise.
        """
        return self.value <= other_number.value

if __name__ == '__main__':
    # Hard-coded sample values for testing the comparison method
    num_a = Number(10)
    num_b = Number(25)
    
    result = num_a.compare(num_b)
    
    print(f"Comparing {num_a.value} with {num_b.value}:")
    if result:
        print("Result is True (first number is less than or equal to second)")
    else:
        print("Result is False (first number is greater than second)")