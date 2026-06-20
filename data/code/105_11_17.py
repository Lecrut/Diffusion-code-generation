from datetime import datetime, timedelta

class DateCalculator:
    def determine_next_monday(self):
        today = datetime.now()
        days_until_monday = (7 - today.weekday()) % 7
        next_monday = today + timedelta(days=days_until_monday)
        return next_monday.strftime('%Y-%m-%d')

if __name__ == '__main__':
    calculator = DateCalculator()
    print(f"Next Monday: {calculator.determine_next_monday()}")