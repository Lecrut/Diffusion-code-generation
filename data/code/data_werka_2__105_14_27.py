import datetime

class NextWeekdayCalculator:
    MONDAY = 0
    SUNDAY = 6

    def __init__(self, reference_date: datetime.date):
        self.reference_date = reference_date

    def calculate_next_monday(self) -> datetime.date:
        current_weekday = self.reference_date.weekday()
        days_until_monday = (self.MONDAY - current_weekday) % 7
        if days_until_monday == 0:
            days_until_monday = 7
        next_monday = self.reference_date + datetime.timedelta(days=days_until_monday)
        return next_monday

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 25)
    calculator = NextWeekdayCalculator(sample_date)
    result = calculator.calculate_next_monday()
    print(result)