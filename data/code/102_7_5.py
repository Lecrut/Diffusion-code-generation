import datetime
import unittest
class TestDateWeekday(unittest.TestCase):
    def is_weekday(self, date_obj):
        return date_obj.weekday() < 5
    def test_weekday_true(self):
        date1 = datetime.datetime(2023, 10, 23)
        self.assertTrue(self.is_weekday(date1))
        date2 = datetime.datetime(2023, 10, 30)
        self.assertTrue(self.is_weekday(date2))
    def test_weekday_false(self):
        date1 = datetime.datetime(2023, 10, 24)
        self.assertTrue(self.is_weekday(date1))
        date2 = datetime.datetime(2023, 10, 29)
        self.assertFalse(self.is_weekday(date2))
    def test_weekday_saturday(self):
        date1 = datetime.datetime(2023, 10, 28)
        self.assertFalse(self.is_weekday(date1))
    def test_weekday_sunday(self):
        date1 = datetime.datetime(2023, 10, 29)
        self.assertFalse(self.is_weekday(date1))
    def test_weekday_monday(self):
        date1 = datetime.datetime(2023, 10, 30)
        self.assertTrue(self.is_weekday(date1))
    def test_weekday_friday(self):
        date1 = datetime.datetime(2023, 10, 27)
        self.assertTrue(self.is_weekday(date1))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)