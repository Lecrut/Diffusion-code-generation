import calendar
import datetime

class DateHelper:
    WEEKDAY_NAMES = [
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
        try:
            date_obj = datetime.date(year, month, day)
            return date_obj.strftime("%A")
        except ValueError:
            raise ValueError(f"Invalid date: {year}-{month}-{day}")

if __name__ == '__main__':
    result = DateHelper.get_weekday_name(2024, 2, 29)
    print(result)