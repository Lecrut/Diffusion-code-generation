import unittest

def get_next_month_first_day(date_string):
    from datetime import datetime, timedelta
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        if date_obj.month == 12:
            return (datetime(date_obj.year + 1, 1, 1) - timedelta(days=1)).strftime('%Y-%m-%d')
        else:
            return datetime(date_obj.year, date_obj.month + 1, 1).strftime('%Y-%m-%d')
    except ValueError as e:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from e

class TestGetNextMonthFirstDay(unittest.TestCase):
    def test_next_month(self):
        self.assertEqual(get_next_month_first_day("2023-10-15"), "2023-11-01")
    
    def test_december_boundary(self):
        self.assertEqual(get_next_month_first_day("2023-12-31"), "2024-01-01")
    
    def test_invalid_date_format(self):
        with self.assertRaises(ValueError) as context:
            get_next_month_first_day("2023/10/15")
        self.assertTrue("Invalid date format" in str(context.exception))

if __name__ == '__main__':
    sample_date1 = "2023-10-15"
    result1 = get_next_month_first_day(sample_date1)
    print(f"{sample_date1}: {result1}")
    
    sample_date2 = "2023-12-31"
    result2 = get_next_month_first_day(sample_date2)
    print(f"{sample_date2}: {result2}")

    unittest.main()