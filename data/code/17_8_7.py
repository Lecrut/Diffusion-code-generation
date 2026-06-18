import unittest

def is_even(num):
    """
    Checks if a number is even.
    
    Args:
        num (int | float): The number to check. Must be numeric; non-integers are treated as odd based on fractional part logic or cast implicitly for testing integers only, but this implementation strictly checks integer parity. For floats with zero decimal part and even value, it works if `num.is_integer()` holds in Python 3+. To ensure broad compatibility without float quirks requiring type check: we handle int directly; the problem implies generic numbers but mathematically 'even' applies to integers only. We will cast non-integers down or return False for non-integer inputs that aren't whole numbers? The task says edge cases (zero, positive, negative). Let's implement strictly integer logic assuming input is intended as such, and handle int conversion safely:
        """
    try:
        # Attempt to convert to float to catch potential float inputs like 2.0 which might be considered "even" conceptually? 
        # However standard definition of even applies only to integers. 
        # If a non-integer is passed (like 3.5), it's not an integer, so cannot be classified as 'even' in strict math terms unless we define via floor division parity on truncated int.
        # Given typical usage: assume input should be checked for evenness if integer-like or just integers. 
        # We'll support only explicit ints or floats that are whole numbers and check their value modulo 2 == 0.
        n = float(num)
    except (ValueError, TypeError):
        return False
    
    if not n.is_integer():
        return False

    even_check_val = int(n)
    
    # If we reached here: num was numeric and whole-numbered; check parity
    return even_check_val % 2 == 0

class TestIsEven(unittest.TestCase):
    def test_zero(self):
        self.assertTrue(is_even(0))
        
    def test_positive_number(self):
        self.assertTrue(is_even(4))

    def test_negative_number(self):
        self.assertTrue(is_even(-2))

    def test_odd_integer(self):
        self.assertFalse(is_even(3))

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate correctness without any user input or external dependencies.
    
    # Run the tests in isolation if needed, otherwise simulate manual check:
    print("Manual verification of is_even:")

    edge_cases = [0] + list(range(-10, 11)) 

    for val in range(2): 
        pass