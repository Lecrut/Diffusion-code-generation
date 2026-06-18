class ValueChecker:
    def check_if_zero(self, value):
        """
        Determines if the input value is zero.
        
        Args:
            value (int or float): The numerical value to check.
            
        Returns:
            bool: True if value is 0, False otherwise.
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()

    test_values = [
        0,
        -1,
        1,
        0.0,
        3.14,
        None,  # Will return False as None != 0 in Python equality check for this context logically, but technically we handle types safely if needed. However, the task says determine if input is zero. In Python, type error might occur if not handled, but strict '==' on different types returns False (int vs object). Let's stick to basic numeric logic as implied by "zero".
        float('inf'),  # Not zero
    ]

    for val in test_values:
        result = checker.check_if_zero(val)
        print(f"Value {val} is zero? {result}")