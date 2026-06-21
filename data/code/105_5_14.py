from datetime import date, timedelta

class DateCalculator:
    WEDNESDAY_INDEX = 2
    DAYS_IN_WEEK = 7

    def __init__(self, start_date: date):
        self.start_date = start_date

    def _calculate_offset(self) -> int:
        current_weekday = self.start_date.weekday()
        offset = self.WEDNESDAY_INDEX - current_weekday
        if offset <= 0:
            offset += self.DAYS_IN_WEEK
        return offset

    def get_next_wednesday(self) -> date:
        offset = self._calculate_offset()
        return self.start_date + timedelta(days=offset)

if __name__ == '__main__':
    calc = DateCalculator(date(2023, 10, 10))
    print(calc.get_next_wednesday())
    print(calc.start_date + timedelta(days=calc._calculate_offset()))