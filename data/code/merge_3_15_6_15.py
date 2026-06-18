def check_equality(a: any, b: any) -> bool:
    """
    Checks if two values are equal using Python's default equality operators.
    
    Supports integers, floats, strings, and other standard types.
    Note: Floats may return False for mathematically equivalent numbers 
    due to floating-point precision issues unless explicitly handled or compared via abs tolerance.
    For strict value comparison without custom logic on type (e.g., 0.1 vs float('0.1')),
    this uses standard '==' which is expected behavior in most general equality checks
    and test suites for such tasks. If floating point tolerance was intended, it should be 
    specified as an argument; here we assume strict value comparison per task constraints.
    
    Args:
        a (any): First value to compare.
        b (any): Second value to compare.
        
    Returns:
        bool: True if a == b is satisfied in Python semantics, False otherwise.
    """
    return a == b

class TestCheckEquality(unittest.TestCase):
    
    def test_integers_equal(self):
        self.assertTrue(check_equality(5, 5))

    def test_integers_not_equal(self):
        self.assertFalse(check_equality(5, 6))

    def test_floats_strictly_equivalent(self):
        # Direct comparison of same float literal should be true. 
        # Avoid issues like 0.1 + 0.2 == 0.3 in general unless specified otherwise for this generic task.
        self.assertTrue(check_equality(5.5, 5.5))

    def test_floats_approximate_not_equal_by_default(self):
        # Without tolerance parameter provided by caller or fixed logic inside function, 
        # floating point arithmetic results may not be strictly equal even if close.
        self.assertFalse(abs(0.1 + 0.2 - 0.3) < float('1e-9') and check_equality(0.1 + 0.2, 0.3))

    def test_strings_equal(self):
        self.assertTrue(check_eequality("hello", "hello"))

    def test_strings_not_equal_case_sensitive(self):
        self.assertFalse(check_equality("Hello", "hello"))

    def test_mixed_types_int_str_no_match(self):
        # In Python, int and string are never equal even if content seems relevant numerically.
        self.assertFalse(check_equality(5, '5'))

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files
    test_data = [
        ((10, 10), True), 
        ((20, 30), False), 
        (("test", "test"), True), 
        (("Test", "TEST"), False),  
        ((4.5, 4.5), True),         
    ]

    # Run the tests with hardcoded samples directly via unittest discovery or manual checks
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCheckEquality)
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(result.errorCode or 1)