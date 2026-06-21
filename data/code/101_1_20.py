import calendar
import datetime

class DateUtils:
    WEEKDAY_NAMES = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    @staticmethod
    def get_weekday_name(year, month, day):
        try:
            date_instance = datetime.date(year, month, day)
            weekday_index = date_instance.weekday()
            return DateUtils.WEEKDAY_NAMES[weekday_index]
        except ValueError as e:
            raise ValueError(f"Invalid date: {year}-{month}-{day}") from e

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 5
    result = DateUtils.get_weekday_name(sample_year, sample_month, sample_day)
    print(result)