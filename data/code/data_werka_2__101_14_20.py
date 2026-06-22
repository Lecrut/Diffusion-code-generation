import datetime
import calendar

class DateAnalyzer:
    DAYS_OF_WEEK = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    @staticmethod
    def get_weekday_name(year: int, month: int, day: int) -> str:
        date_instance = datetime.date(year, month, day)
        weekday_index = date_instance.weekday()
        return DateAnalyzer.DAYS_OF_WEEK[weekday_index]

if __name__ == '__main__':
    target_year = 2025
    target_month = 3
    target_day = 15
    computed_weekday = DateAnalyzer.get_weekday_name(target_year, target_month, target_day)
    print(computed_weekday)