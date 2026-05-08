import unittest
def calculate_year_difference(year1, year2):
    return year2 - year1
class TestYearDifference(unittest.TestCase):
    def test_positive_difference(self):
        self.assertEqual(calculate_year_difference(2000, 2020), 20)
        self.assertEqual(calculate_year_difference(1990, 2010), 20)
    def test_negative_difference(self):
        self.assertEqual(calculate_year_difference(2020, 2000), -20)
        self.assertEqual(calculate_year_difference(2010, 2000), -10)
    def test_zero_difference(self):
        self.assertEqual(calculate_year_difference(2000, 2000), 0)
    def test_large_difference(self):
        self.assertEqual(calculate_year_difference(100, 2000), 1900)
        self.assertEqual(calculate_year_difference(1000, 500), -500)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)