def check_equality(a, b):
    """
    Returns a boolean indicating whether two values of any type 
    (integers, floats, strings) are equal.
    
    Args:
        a: The first value to compare.
        b: The second value to compare.
        
    Returns:
        bool: True if a is equal to b, False otherwise.
    """
    return a == b

class TestCheckEquality(unittest.TestCase):
    def test_integer_equality(self):
        self.assertEqual(check_equality(5, 5), True)
        self.assertEqual(check_equality(0, 0), True)
        self.assertEqual(check_equality(-10, -10), True)

    def test_float_equality(self):
        self.assertEqual(check_equality(3.14, 3.14), True)
        self.assertAlmostEqual(check_equality(2.5, 2.5), True)
        self.assertFalse(check_equality(1.7, 1.8))

    def test_string_equality(self):
        self.assertEqual(check_equality("hello", "hello"), True)
        self.assertEqual(check_equality("", ""), True)
        self.assertTrue(check_equality("test string here", "test string here"))
        
    def test_mismatched_types_int_float_strong_value_match(self):
        # Testing int and float with same numeric value in memory (e.g. 5 == 5.0)
        self.assertEqual(check_equality(5, 5.0), True)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCheckEquality)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)