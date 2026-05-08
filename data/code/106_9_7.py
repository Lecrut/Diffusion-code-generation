import unittest
def calculate_year_difference(year1, year2):
    return year2 - year1
class TestYearDifference(unittest.TestCase):
    def test_positive_difference(self):
        self.assertEqual(calculate_year_difference(2000, 2020), 20)
    def test_negative_difference(self):
        self.assertEqual(calculate_year_difference(2020, 2000), -20)
    def test_difference_with_larger_numbers(self):
        self.assertEqual(calculate_year_difference(1990, 2023), 33)
    def test_difference_with_smaller_numbers(self):
        self.assertEqual(calculate_year_difference(1980, 1950), -30)
    def test_difference_of_zero(self):
        self.assertEqual(calculate_year_difference(2010, 2010), 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)