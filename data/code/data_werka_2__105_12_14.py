from datetime import datetime, timedelta

class WeekdayCalculator:
    def __init__(self, reference_date_str):
        self.reference_date = datetime.strptime(reference_date_str, '%Y-%m-%d')

    def next_occurrence(self, target_weekday):
        current_weekday = self.reference_date.weekday()
        days_ahead = (target_weekday - current_weekday + 7) % 7
        if days_ahead == 0:
            days_ahead = 7
        next_date = self.reference_date + timedelta(days=days_ahead)
        return next_date.strftime('%Y-%m-%d')

    def days_until(self, target_weekday):
        current_weekday = self.reference_date.weekday()
        days_ahead = (target_weekday - current_weekday + 7) % 7
        if days_ahead == 0:
            days_ahead = 7
        return days_ahead

if __name__ == '__main__':
    calculator = WeekdayCalculator('2023-10-01')
    print(calculator.next_occurrence(4))
    print(calculator.days_until(4))