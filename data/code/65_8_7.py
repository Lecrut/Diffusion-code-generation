from unittest import TestCase, main as unittest_main

CONVERSION_FACTOR = 12

def convert_feet_to_inches(feet_value):
    if not isinstance(feet_value, (int, float)):
        raise TypeError("Input must be a number")
    if feet_value < 0:
        raise ValueError("Feet cannot be negative")
    return feet_value * CONVERSION_FACTOR

class TestConversion(TestCase):
    def test_hardcoded_case(self):
        input_val = 12
        expected = 144
        computed = convert_feet_to_inches(input_val)
        self.assertEqual(computed, expected)

if __name__ == '__main__':
    sample_feet = 12
    inches = convert_feet_to_inches(sample_feet)
    unittest_main(argv=['first-arg-is-ignored'], exit=False)
    print(inches)