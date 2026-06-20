from datetime import datetime

class DateValidator:
    WEEKDAY_DAYS = set(range(5))

    @staticmethod
    def is_weekday(date_string: str) -> bool:
        try:
            date_obj = datetime.strptime(date_string, '%Y-%m-%d')
            return date_obj.weekday() in DateValidator.WEEKDAY_DAYS
        except ValueError:
            raise ValueError('Invalid Date Format')

if __name__ == '__main__':
    validator = DateValidator()
    dates_to_check = [
        "2023-10-23",
        "2023-10-29",
        "2023-10-28",
        "2023-10-27",
        "2023-10-28",
        "2023-10-30"
    ]
    for date in dates_to_check:
        print(f"{date}: {validator.is_weekday(date)}")