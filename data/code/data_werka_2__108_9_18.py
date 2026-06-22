from datetime import datetime
from typing import Union
import calendar

class DayOfMonthCalculator:
    def __init__(self, date_instance: datetime) -> None:
        self.date_instance = date_instance

    def get_day_number(self) -> int:
        return self.date_instance.day

    def get_calendar_day_name(self) -> str:
        return calendar.day_name[self.date_instance.weekday()]

    def is_end_of_month(self) -> bool:
        last_day = calendar.monthrange(self.date_instance.year, self.date_instance.month)[1]
        return self.date_instance.day == last_day

if __name__ == '__main__':
    sample_dt = datetime(2024, 2, 29, 14, 0, 0)
    calculator = DayOfMonthCalculator(sample_dt)
    print(calculator.get_day_number())
    print(calculator.get_calendar_day_name())
    print(calculator.is_end_of_month())