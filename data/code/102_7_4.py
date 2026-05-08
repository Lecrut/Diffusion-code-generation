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
        date6 = datetime.datetime(2023, 11, 1)
        self.assertTrue(self.is_weekday(date6))
        date7 = datetime.datetime(2023, 11, 2)
        self.assertTrue(self.is_weekday(date7))
        date8 = datetime.datetime(2023, 11, 3)
        self.assertTrue(self.is_weekday(date8))
        date9 = datetime.datetime(2023, 11, 4)
        self.assertTrue(self.is_weekday(date9))
        date10 = datetime.datetime(2023, 11, 5)
        self.assertFalse(self.is_weekday(date10))
    def test_weekday_specific_days(self):
        monday = datetime.datetime(2023, 10, 23)
        self.assertTrue(self.is_weekday(monday))
        saturday = datetime.datetime(2023, 10, 28)
        self.assertTrue(self.is_weekday(saturday))
        sunday = datetime.datetime(2023, 10, 29)
        self.assertTrue(self.is_weekday(sunday))
        self.assertTrue(self.is_weekday(datetime.datetime(2023, 10, 28)))
        self.assertTrue(self.is_weekday(datetime.datetime(2023, 10, 29)))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)