from datetime import datetime, timedelta

class MonthTimeCalculator:
    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month
        self.start_date = datetime(year, month, 1)
        if month == 12:
            self.end_date = datetime(year + 1, 1, 1) - timedelta(seconds=1)
        else:
            self.end_date = datetime(year, month + 1, 1) - timedelta(seconds=1)

    def total_duration(self) -> timedelta:
        return self.end_date - self.start_date

    def remaining_time(self, current: datetime) -> timedelta:
        if current < self.start_date:
            return self.total_duration()
        if current > self.end_date:
            return timedelta(0)
        return self.end_date - current

if __name__ == '__main__':
    calculator = MonthTimeCalculator(2023, 10)
    print(calculator.total_duration())
    print(calculator.remaining_time(datetime(2023, 10, 15, 12, 0, 0)))
    print(calculator.remaining_time(datetime(2023, 10, 1, 0, 0, 0)))
    print(calculator.remaining_time(datetime(2023, 10, 31, 23, 59, 59)))
    print(calculator.remaining_time(datetime(2023, 11, 1, 0, 0, 0)))