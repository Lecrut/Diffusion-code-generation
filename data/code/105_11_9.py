from datetime import date, timedelta

MONDAY_INDEX = 0
WEEK_LENGTH = 7

class DateCalculator:
    def __init__(self, reference_date=None):
        self.reference_date = reference_date if reference_date is not None else date.today()

    def get_next_monday(self):
        current_weekday = self.reference_date.weekday()
        days_offset = (MONDAY_INDEX - current_weekday) % WEEK_LENGTH
        if days_offset == 0:
            days_offset = WEEK_LENGTH
        return self.reference_date + timedelta(days=days_offset)

if __name__ == '__main__':
    calculator = DateCalculator(date(2023, 10, 15))
    result = calculator.get_next_monday()
    print(result.isoformat())