import datetime

class DateAnalyzer:
    WEEKDAY_NAMES = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    )

    @staticmethod
    def _validate_date(year, month, day):
        if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
            raise ValueError("Inputs must be integers")
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
        try:
            return datetime.date(year, month, day)
        except ValueError as e:
            raise ValueError(f"Invalid date: {e}")

    def __init__(self, year, month, day):
        self.date_obj = self._validate_date(year, month, day)

    def get_weekday_name(self):
        return self.WEEKDAY_NAMES[self.date_obj.weekday()]

if __name__ == '__main__':
    analyzer = DateAnalyzer(2023, 10, 10)
    print(analyzer.get_weekday_name())