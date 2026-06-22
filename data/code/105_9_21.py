from datetime import date, timedelta

class DateCalculator:
    def __init__(self, reference_date: date):
        self.reference_date = reference_date

    def get_next_monday(self) -> date:
        current_weekday = self.reference_date.weekday()
        days_until_monday = (7 - current_weekday) % 7
        if days_until_monday == 0:
            days_until_monday = 7
        return self.reference_date + timedelta(days=days_until_monday)

    def get_next_monday_formatted(self) -> str:
        next_monday = self.get_next_monday()
        return next_monday.strftime('%Y-%m-%d')

if __name__ == '__main__':
    calculator = DateCalculator(date(2024, 2, 28))
    print(calculator.get_next_monday())
    print(calculator.get_next_monday_formatted())