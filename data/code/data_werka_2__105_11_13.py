from datetime import date, timedelta
class MondayCalculator:
    def __init__(self, anchor_date=None):
        if anchor_date is None:
            anchor_date = date.today()
        self.anchor = anchor_date
    def compute_next_monday(self):
        weekday_index = self.anchor.weekday()
        days_ahead = (7 - weekday_index) % 7
        if days_ahead == 0:
            days_ahead = 7
        return self.anchor + timedelta(days=days_ahead)
if __name__ == '__main__':
    calculator = MondayCalculator(date(2024, 1, 1))
    next_monday = calculator.compute_next_monday()
    print(next_monday.isoformat())