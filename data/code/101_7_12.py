import datetime

class WeekdayCalculator:
    def __init__(self, factory):
        self._factory = factory
    
    def get_weekday(self, year, month, day):
        date_object = datetime.date(year, month, day)
        return self._factory.get_day_of_week(date_object)

class DayOfWeekFactory:
    def get_day_of_week(self, date_object):
        return date_object.weekday()

if __name__ == '__main__':
    factory = DayOfWeekFactory()
    calculator = WeekdayCalculator(factory)
    print(calculator.get_weekday(2024, 7, 4))