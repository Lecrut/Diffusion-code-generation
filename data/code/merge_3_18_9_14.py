class Number:
    def __init__(self, value):
        """Initialize a Number object with an integer value."""
        self.value = int(value)
    
    def compare(self, other_number):
        """Compare this number against another number passed as an argument.
        
        Returns a tuple (is_greater, is_equal, is_less).
        
        Args:
            other_number: A Number object to compare against.
            
        Returns:
            Tuple of three booleans indicating if self > other, self == other, or self < other.
        """
        return self.value > other_number.value, \
               self.value == other_number.value, \
               self.value < other_number.value

if __name__ == '__main__':
    # Hard-coded sample values for testing the Number class comparison method
    
    num_a = Number(10)
    num_b = Number(5)
    
    result = num_a.compare(num_b)
    
    print(f"Comparing {num_a.value} vs {num_b.value}:")
    if result[0]:
        print("Greater: True, Equal: False, Less: False")
    elif result[1]:
        print("Greater: False, Equal: True, Less: False")
    else:
        print("Greater: False, Equal: False, Less: True")