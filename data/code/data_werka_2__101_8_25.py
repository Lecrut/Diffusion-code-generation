import calendar
import datetime

class DateConverter:
    _MONTHS_PER_YEAR = 12
    _DAYS_PER_WEEK = 7
    
    def __init__(self, year: int, month: int, day: int):
        self._verify_date(year, month, day)
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def _verify_date(y: int, m: int, d: int) -> None:
        try:
            datetime.date(y, m, d)
        except ValueError as e:
            raise ValueError(f"Invalid date provided: ({y}, {m}, {d})") from e

    def get_weekday_name(self) -> str:
        weekday_idx = calendar.weekday(self.year, self.month, self.day)
        return calendar.day_name[weekday_idx]

if __name__ == '__main__':
    converter = DateConverter(2025, 5, 20)
    name = converter.get_weekday_name()
    print(name)