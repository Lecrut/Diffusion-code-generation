from datetime import datetime, timedelta

class DateCalculator:
    def determine_next_date(self, days):
        today = datetime.now()
        next_date = today + timedelta(days=days)
        return next_date.isoformat()

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.determine_next_date(10))
    print(calculator.determine_next_date(2))
    print(calculator.determine_next_date(1))