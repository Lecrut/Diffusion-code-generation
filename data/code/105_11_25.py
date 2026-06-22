from datetime import date, timedelta

class MondayCalculator:
    def __init__(self, reference_date=None):
        self.reference_date = reference_date if reference_date is not None else date.today()

    def compute_next_monday(self):
        current_weekday = self.reference_date.weekday()
        days_offset = (7 - current_weekday) % 7
        if days_offset == 0:
            days_offset = 7
        return self.reference_date + timedelta(days=days_offset)

if __name__ == '__main__':
    calculator = MondayCalculator(date(2024, 5, 20))
    next_monday = calculator.compute_next_monday()
    print(next_monday.isoformat())