class Number:
    """A class representing a number with comparison capabilities."""
    
    def __init__(self, value):
        """Initialize the Number object with an integer or float value."""
        self.value = int(value) if isinstance(value, (int, float)) else value
    
    def compare(self, other_number: 'Number') -> bool:
        """Compare this number against another passed as a Number argument.
        
        Returns True if this number is strictly greater than the other, False otherwise.
        
        Args:
            other_number: A Number object to compare against.
            
        Returns:
            Boolean indicating whether self.value > other_number.value.
        """
        return self.value > other_number.value

if __name__ == '__main__':
    # Hard-coded sample values for testing the comparison method
    num_a = Number(10)
    num_b = Number(5)
    
    result = num_a.compare(num_b)
    
    print(f"Comparing {num_a} with {num_b}")
    if result:
        print("Result: The first number is greater.")
    else:
        print("Result: The first number is not strictly greater than the second.")