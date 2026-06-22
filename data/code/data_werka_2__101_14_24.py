import calendar
import datetime

class DateResolver:
    def __init__(self, year: int, month: int, day: int):
        self.year = year
        self.month = month
        self.day = day
        self.date_obj = datetime.date(year, month, day)

    def get_day_of_week(self) -> str:
        weekday_index = self.date_obj.weekday()
        return calendar.day_name[weekday_index]

    def get_iso_calendar(self) -> tuple:
        return self.date_obj.isocalendar()

if __name__ == '__main__':
    resolver = DateResolver(2025, 3, 15)
    day_name = resolver.get_day_of_week()
    iso_year, iso_week, iso_weekday = resolver.get_iso_calendar()
    print(day_name)
    print(iso_year, iso_week, iso_weekday)