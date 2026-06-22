from datetime import date, timedelta

class MondayCalculator:
    def __init__(self, reference: date = None):
        if reference is None:
            reference = date.today()
        self.reference = reference

    def get_next_monday(self) -> date:
        current_weekday = self.reference.weekday()
        days_ahead = 7 - current_weekday
        if days_ahead == 7:
            days_ahead = 0
        return self.reference + timedelta(days=days_ahead)

if __name__ == '__main__':
    calculator = MondayCalculator(date(2023, 10, 15))
    result = calculator.get_next_monday()
    print(result.isoformat())