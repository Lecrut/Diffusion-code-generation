from datetime import date, timedelta

class MondayCalculator:
    def __init__(self, reference_date=None):
        self.reference_date = reference_date if reference_date is not None else date.today()
    
    def get_upcoming_monday(self):
        current_weekday = self.reference_date.weekday()
        days_to_add = (7 - current_weekday) % 7
        if days_to_add == 0:
            days_to_add = 7
        return self.reference_date + timedelta(days=days_to_add)

if __name__ == '__main__':
    calculator = MondayCalculator(date(2023, 10, 15))
    result = calculator.get_upcoming_monday()
    print(result.isoformat())