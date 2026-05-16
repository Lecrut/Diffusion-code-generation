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
        date3 = datetime.datetime(2023, 10, 24)
        self.assertTrue(self.is_weekday(date3))
        date4 = datetime.datetime(2023, 10, 29)
        self.assertTrue(self.is_weekday(date4))
        date5 = datetime.datetime(2023, 10, 31)
        self.assertTrue(self.is_weekday(date5))
        date6 = datetime.datetime(2023, 10, 31)
        self.assertTrue(self.is_weekday(date6))
        date7 = datetime.datetime(2023, 10, 31)
        self.assertTrue(self.is_weekday(date7))
        date8 = datetime.datetime(2023, 10, 31)
        self.assertTrue(self.is_weekday(date8))
        date9 = datetime.datetime(2023, 10, 31)
        self.assertTrue(self.is_weekday(date9))
        date10 = datetime.datetime(2023, 10, 31)
        self.assertTrue(self.is_weekday(date10))
        date11 = datetime.datetime(2023, 10, 31)
        self.assertTrue(self.is_weekday(date11))
        date12 = datetime.datetime(2023, 10, 31)
        self.assertTrue(self.is_weekday(date12))
        date13 = datetime.datetime(2023, 10, 31)
        self.assertTrue(self.is_weekday(date13))
        date14 = datetime.datetime(2023, 10, 31)
        self.assertTrue(self.is_weekday(date14))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)