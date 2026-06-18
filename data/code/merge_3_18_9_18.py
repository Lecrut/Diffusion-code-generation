class Number:
    """A class representing a number with comparison capabilities."""
    
    def __init__(self, value):
        """Initialize the Number object with an integer or float value."""
        self.value = int(value) if isinstance(value, (int, float)) else value
    
    def compare(self, other_number: 'Number') -> str:
        """Compare this number against another Number passed as argument.
        
        Args:
            other_number: Another Number object to compare against.
            
        Returns:
            A string indicating the relationship between self and other_number.
            Possible values are "self is greater", "self is equal", or "self is smaller".
        """
        if isinstance(other_number, Number):
            comparison = self.value > other_number.value
            equality = self.value == other_number.value
            
            if comparison:
                return f"{type(self).__name__}({self.value}) is greater than {type(other_number).__name__}({other_number.value})"
            elif not comparison and equality:
                return f"{type(self).__name__}({self.value}) is equal to {type(other_number).__name__}({other_number.value})"
            else:
                return f"{type(self).__name__}({self.value}) is smaller than {type(other_number).__name__}({other_number.value})"
        else:
            raise TypeError("Argument must be an instance of Number")

if __name__ == '__main__':
    # Hard-coded sample values for testing the comparison functionality
    
    num_a = Number(10)
    num_b = Number(25)
    num_c = Number(30)
    
    print("Comparing 10 and 25:")
    result_1 = num_a.compare(num_b)
    print(result_1)
    
    print("\nComparing 25 and 30:")
    result_2 = num_b.compare(num_c)
    print(result_2)
    
    print("\nComparing equal values (30 vs 30):")
    num_d = Number(30)
    result_3 = num_a.compare(num_d)
    print(result_3)