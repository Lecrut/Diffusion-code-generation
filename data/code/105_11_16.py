from datetime import datetime, timedelta

class DateCalculator:
    def determine_next_date(self, days):
        today = datetime.now()
        days_until_monday = (7 - today.weekday()) % 7
        next_monday = today + timedelta(days=days_until_monday + days)
        return next_monday.isoformat()

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.determine_next_date(0))
    print(calculator.determine_next_date(10))
    print(calculator.determine_next_date(2))