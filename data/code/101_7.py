import datetime
class DateCalculatorFactory:
    def get_day_of_week(self, date_object):
        return date_object.weekday()
class DateCalculator:
    def __init__(self, factory):
        self._factory = factory
    def get_day_of_week(self, date_object):
        return self._factory.get_day_of_week(date_object)
if __name__ == '__main__':
    class MockDate:
        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day
            self.date = datetime.date(year, month, day)
    class MockDateTime:
        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day
            self.date = datetime.date(year, month, day)
    factory = DateCalculatorFactory()
    calculator = DateCalculator(factory)
    date1 = MockDate(2023, 10, 26)
    date2 = MockDateTime(1999, 1, 1)
    day1 = calculator.get_day_of_week(date1.date)
    day2 = calculator.get_day_of_week(date2.date)
    print(f"Day of the week for {date1.date}: {day1}")
    print(f"Day of the week for {date2.date}: {day2}")