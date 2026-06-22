import unittest

def feet_to_inches(feet):
    return feet * 12

class TestConversion(unittest.TestCase):
    def test_12_feet_to_inches(self):
        result = feet_to_inches(12)
        self.assertEqual(result, 144)

if __name__ == '__main__':
    sample_feet = 12
    inches = feet_to_inches(sample_feet)
    print(inches)
    unittest.main()