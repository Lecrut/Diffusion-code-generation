class Number:
    def __init__(self, value):
        """Initialize a Number object with an integer value."""
        self.value = int(value)

    def compare(self, other_number):
        """Compare this number against another passed as argument.
        
        Returns:
            'greater' if this is greater than the other.
            'less' if this is less than the other.
            'equal' if both are equal.
        """
        # Ensure other_number is also a Number instance for type safety, 
        # though it could accept any numeric-like object with __gt__ or similar logic.
        # For strict adherence to "object representing a number", we assume input matches self's type.
        
        if isinstance(other_number, Number):
            return 'greater' if self.value > other_number.value else \
                   ('less' if self.value < other_number.value else 'equal')
        elif hasattr(other_number, '__gt__'):
            # Fallback for direct numeric comparison if passed a raw int/float (optional flexibility)
            return 'greater' if self.value > other_number else \
                   ('less' if self.value < other_number else 'equal')
        else:
            raise TypeError("Comparison requires another Number object or numeric value.")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    num_a = Number(10)
    num_b = Number(5)
    num_c = Number(20)
    num_d = Number(10)  # Equal to num_a

    print(f"Comparing {num_a} and {num_b}:")
    result_ab = num_a.compare(num_b)
    if result_ab == 'greater':
        print("Result: First number is greater.")
    elif result_ab == 'less':
        print("Result: First number is less.")
    else:
        print("Result: Numbers are equal.")

    print(f"\nComparing {num_c} and {num_a}:")
    result_ca = num_c.compare(num_a)
    if result_ca == 'greater':
        print("Result: First number is greater.")
    elif result_ca == 'less':
        print("Result: First number is less.")
    else:
        print("Result: Numbers are equal.")

    print(f"\nComparing {num_a} and itself:")
    result_aa = num_a.compare(num_d)  # Using a copy to simulate self comparison logic visually if needed, 
                                     # but here we compare with an identical value object.
    if result_aa == 'greater':
        print("Result: First number is greater.")
    elif result_aa == 'less':
        print("Result: First number is less.")
    else:
        print("Result: Numbers are equal.")