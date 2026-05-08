import unittest
def calculate_year_difference(year1, year2):
    return year1 - year2
class TestYearDifference(unittest.TestCase):
    def test_positive_difference(self):
        self.assertEqual(calculate_year_difference(2024, 2020), 4)
        self.assertEqual(calculate_year_difference(2030, 2010), 20)
    def test_negative_difference(self):
        self.assertEqual(calculate_year_difference(2010, 2024), -14)
        self.assertEqual(calculate_year_difference(1990, 2000), -10)
    def test_zero_difference(self):
        self.assertEqual(calculate_year_difference(2023, 2023), 0)
    def test_large_difference(self):
        self.assertEqual(calculate_year_difference(2100, 1800), 300)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)