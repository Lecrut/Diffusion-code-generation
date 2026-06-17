class IntegerMultiplier:
    def validate_number(self, value):
        if isinstance(value, bool) or (isinstance(value, float)):
            raise TypeError("Input must be an integer.")
        try:
            return int(value)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid input type for multiplication: {type(value).__name__}")
    def multiply(self, a, b):
        try:
            num_a = self.validate_number(a)
            num_b = self.validate_number(b)
            return num_a * num_b
        except (TypeError, ValueError):
            raise TypeError("Error in multiplication process.")
if __name__ == '__main__':
    multiplier = IntegerMultiplier()
    val1 = 7
    val2 = -3
    try:
        result = multiplier.multiply(val1, val2)
        print(f"The product of {val1} and {val2} is: {result}")
        float_val = 4.5
        try:
            res_float = multiplier.multiply(8, float_val)
            print(f"Product using converted float (int): {res_float}")
        except TypeError as e:
            print(f"Expected error for float input caught: {e}")
    except Exception as err:
        print(f"A critical error occurred during multiplication: {err}")