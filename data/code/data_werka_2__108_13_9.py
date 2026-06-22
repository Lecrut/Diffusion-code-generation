from datetime import date
from dataclasses import dataclass

@dataclass
class CalendarDay:
    year: int
    month: int
    day: int

    def numeric_day_of_month(self) -> int:
        return self.day

if __name__ == '__main__':
    sample_date = CalendarDay(year=2024, month=10, day=10)
    print(sample_date.numeric_day_of_month())
    print(sample_date.day)