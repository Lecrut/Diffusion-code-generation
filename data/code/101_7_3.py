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
    class ConcreteDateCalculatorFactory:
        def get_day_of_week(self, date_object):
            return date_object.weekday()
    factory = ConcreteDateCalculatorFactory()
    calculator = DateCalculator(factory)
    date1 = datetime.date(2023, 10, 26)
    date2 = datetime.date(1999, 1, 1)
    date3 = datetime.date(2024, 12, 31)
    day1 = calculator.get_day_of_week(date1)
    day2 = calculator.get_day_of_week(date2)
    day3 = calculator.get_day_of_week(date3)
    print(f"Day of the week for {date1}: {day1}")
    print(f"Day of the week for {date2}: {day2}")
    print(f"Day of the week for {date3}: {day3}")