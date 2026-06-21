from datetime import date, timedelta

class MondayCalculator:
    def __init__(self, start_date=None):
        self.start_date = start_date if start_date is not None else date.today()

    def compute_next_monday(self):
        current_weekday = self.start_date.weekday()
        days_offset = (7 - current_weekday) % 7
        if days_offset == 0:
            days_offset = 7
        return self.start_date + timedelta(days=days_offset)

if __name__ == '__main__':
    calculator = MondayCalculator(date(2023, 10, 1))
    result = calculator.compute_next_monday()
    print(result.isoformat())