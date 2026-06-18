class Number:
    def __init__(self, value):
        """Initialize a Number object with an integer value."""
        self.value = int(value) if isinstance(value, (int, float)) else value
    
    def compare(self, other_value, comparison_operator='=='):
        """Compare this number's value against another provided as argument.
        
        Args:
            other_value (Number or int/float): The object to compare against.
            comparison_operator (str): One of '>', '<', '=', or '!='. Default is '='.
            
        Returns:
            bool: Result of the comparison operation between self.value and other_value's value.
        """
        # Handle if other_value is already a Number instance, otherwise convert it
        try:
            other = float(other_value)
        except (TypeError, ValueError):
            raise TypeError(f"Comparison failed for object {other_value!r} of type {type(other_value).__name__}")

        comparisons = {
            '>': self.value > other,
            '<': self.value < other,
            '=': self.value == other,
            '!=': self.value != other
        }
        
        return comparisons.get(comparison_operator.lower(), NotImplemented)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    num1 = Number(10)
    num2 = Number(5)

    print(f"Comparing {num1.value} with {num2.value}")