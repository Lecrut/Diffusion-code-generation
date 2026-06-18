class Number:
    def __init__(self, value):
        """Initialize a Number object with an integer value."""
        self.value = int(value)

    def compare(self, other_number):
        """Compare this number against another passed as argument.
        
        Args:
            other_number (Number or int): The number to compare against.
            
        Returns:
            str: A string indicating the relationship between the two numbers.
                 - "Equal" if both are equal.
                 - "Less than" if this is smaller.
                 - "Greater than" if this is larger.
        """
        # Convert other_number to int for comparison consistency
        other_value = int(other_number)

        if self.value == other_value:
            return f"{self.value} Equal {other_value}"
        elif self.value < other_value:
            return f"{self.value} Less than {other_value}"
        else:
            return f"{self.value} Greater than {other_value}"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    num1 = Number(5)
    num2 = Number(3)
    
    print(f"Comparing 5 and 3:")
    result = num1.compare(num2)
    print(result)

    num3 = Number("7")
    num4 = Number(9)

    print("\nComparing '7' (as string input during init) and 9:")
    result2 = num3.compare(num4)
    print(result2)
    
    # Test equality case explicitly with same value objects created separately
    a = Number(10)
    b = Number(10)

    print("\nComparing two separate instances of 10:")
    result3 = a.compare(b)
    print(result3)